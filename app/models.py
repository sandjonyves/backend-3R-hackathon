from django.db import models
from account.models import Admin, Agent, Client


# Create your models here.


from django.db import models
from account.models import Admin
from django.utils import timezone
from datetime import timedelta


class SubscriptionAdmin(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)
    start_subscribe = models.DateField(auto_now_add=True) 
    end_subscribe = models.DateField( null=True) 
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
    

        self.end_subscribe = timezone.now().date() + timedelta(days=30)
        self.status = True

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Subscription by {self.admin_id} from {self.start_subscribe} to {self.end_subscribe}, Status: {self.status}'



class SubscriptionClient(models.Model):
    admin_id = models.IntegerField()
    client_id = models.OneToOneField(Client,on_delete=models.CASCADE)
    start_subscribe = models.DateField(auto_now_add=True) 
    end_subscribe = models.DateField(null=True)  
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
 
        self.end_subscribe = timezone.now().date() + timedelta(days=30)
        self.status = True
    
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Subscription by {self.admin_id} from {self.start_subscribe} to {self.end_subscribe}, Status: {self.status}'

class Collection(models.Model):
    agent_id = models.IntegerField()
    client_ids = models.ManyToManyField(Client)
    passing_date = models.DateField(auto_created=True,null=True)



class calender(models.Model):
    name_kwattar = models.CharField(max_length=255)
    days = models.CharField(max_length=255)
    hours = models.CharField(max_length=255)

# class calender(models.Model):
#     # number_day = models.IntegerField()
#     days = models.CharField(max_length=255)
#     hours = models.CharField(max_length=255)
