
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,get_user_model,login
from django.contrib.auth.models import Permission,Group


from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.status import HTTP_404_NOT_FOUND

from .permissions import group_permissionOfcathegorie_piece 
from .models import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# from store.serializers import CommandeSerializer

#serializeur du client
class UserSerializer(serializers.ModelSerializer):
    # user_type = serializers.IntegerField(write_only = True)
    class Meta:
        model = CustomUser
        fields = ('id','username','email','phone_number','password','role')

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('__all__')


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('__all__')

class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('__all__')
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')

class UserLoginSerializer(TokenObtainPairSerializer):
    email = serializers.CharField()
    password = serializers.CharField()


# class OtherClientSerializer(serializers.ModelSerializer):

#     # commandes  = CommandeSerializer(read_only=True )
#     class Meta:
#         model = OtherClient
#         fields = ('id','username','email','phone_number')

#     def create(self,validated_data):
#         email = validated_data['email']
#         # print(email)
#         other_client,created = OtherClient.objects.get_or_create(email=email,defaults = validated_data)
#         print(other_client)
#         if ( not created):
#             return other_client
#         else:
#             return other_client
        
           

          

    # def validate(self, request):
    #     print(request)
    #     username = request.get('username')
    #     password = request.get('password')

    #     user = authenticate(username=username, password=password)

    #     if not user:
    #         raise serializers.ValidationError('data is not valid')
    #     if not user.is_active:
    #         raise serializers.ValidationError('user is not activated ')
    #     login(request,user)
    #     token = self.get_token(user)
    #     token['is_activate']=user.is_active
    #     token['is_staff']=user.is_staff
    #     token['is_superuser']=user.is_superuser

    #     return {
    #         'refresh': str(token),
    #         'access': str(token.access_token),
    #     }

