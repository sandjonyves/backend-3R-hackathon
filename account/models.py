from typing import Any, Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin,AbstractBaseUser
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse e-mail doit être spécifiée.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    phone_number = models.CharField(max_length=32,null =True)
    username = models.CharField(max_length=32)
    # firstName = models.CharField( ("first name"), max_length=150, blank=True)
    # lastName = models.CharField(("last name"), max_length=150, blank=True)
    email = models.EmailField(("email address"), unique = True)
    bonus = models.IntegerField(blank=True,default=0)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    is_staff = models.BooleanField(
        ("staff status"),
        default=False,
        help_text=("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        ("active"),
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(("date joined"), default=timezone.now)

    objects = CustomUserManager()

  
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']




    class Role(models.TextChoices):
       CLIENT = "CLIENT","client"
       AGENT = "AGENT","agent"
       ADMIN = "ADMIN","admin"
       SUPERUSER = 'SUPERUSER','superuser'
    role = models.CharField( max_length=32,choices =Role.choices,default="")
    
    # REQUIRED_FIELDS =['firstName','lastName']
    EMAIL_FIELD = 'email'




class ClientManager(models.Manager):
   def get_queryset(self,*arg,**kwargs) -> models.QuerySet:
      return super().get_queryset(*arg,**kwargs).filter(role=CustomUser.Role.CLIENT)    

#table des clients
class Client(CustomUser):
  objects = ClientManager()
  class Meta:
     proxy = True
  def save(self,*args,**kwargs) -> None:
      if not self.pk:
        self.role = CustomUser.Role.CLIENT
      return super().save(*args,**kwargs)

    # user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='client')
    # base_role = CustomUser.Role.CLIENT

#class de management pour filtre les Agent
class AgentManager(models.Manager):
   def get_queryset(self,*arg,**kwargs) -> models.QuerySet:
      return super().get_queryset(*arg,**kwargs).filter(role=CustomUser.Role.AGENT)    
#table des Agents
class Agent(CustomUser):
  objects = AgentManager()

  class Meta:
     proxy = True
  
  def save(self,*args,**kwargs) -> None:
      if not self.pk:
        self.role = CustomUser.Role.AGENT
      return super().save(*args,**kwargs)



#class de management pour filtre les admins
class AdminManager(models.Manager):
   def get_queryset(self,*arg,**kwargs) -> models.QuerySet:
      return super().get_queryset(*arg,**kwargs).filter(role=CustomUser.Role.ADMIN)    


#table des administarteurs 
class Admin(CustomUser):
  objects = AdminManager()
  class Meta:
     proxy = True

  def save(self,*args,**kwargs) -> None:
      if not self.pk:
        self.role = CustomUser.Role.ADMIN
      return super().save(*args,**kwargs)



class SuperuserManager(models.Manager):
   def get_queryset(self,*arg,**kwargs) -> models.QuerySet:
      return super().get_queryset(*arg,**kwargs).filter(role=CustomUser.Role.SUPERUSER)    


#table des administarteurs 
class Superuser(CustomUser):
  objects = SuperuserManager()
  class Meta:
     proxy = True

  def save(self,*args,**kwargs) -> None:
      if not self.pk:
        self.role = CustomUser.Role.SUPERUSER
      return super().save(*args,**kwargs)





# class OtherClient(models.Model):
#   firstName = models.CharField(max_length  = 256)
#   lastName = models.CharField(max_length  = 256)
#   email = models.CharField(max_length = 256)
#   phone_number = models.CharField(max_length = 256)

#   REQUIRED_FIELDS =['firstName','lastName','email','phone_number']






