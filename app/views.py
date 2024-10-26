from rest_framework import viewsets
import rest_framework.permissions
from rest_framework.response import Response
from rest_framework import status
from app.models import calender, Collection, SubscriptionAdmin, SubscriptionClient
from app.serializers import (CalenderSerailizers, CollectionSerializer,
    SubscriptionAdminSerializer, SubscriptionClientSerializer)
from account.models import Client
from rest_framework.permissions import AllowAny
from django.utils import timezone

class SubscriptionAdminViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = SubscriptionAdminSerializer


    def get_queryset(self):
      
        return SubscriptionAdmin.objects.filter(end_subscribe=timezone.now().date())
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
     
        if instance.end_subscribe <= timezone.now().date():
            return Response({"detail": "L'abonnement a expiré."}, status=404)
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class SubscriptionClientViewSet(viewsets.ModelViewSet):

    permission_classes=[AllowAny]
    serializer_class = SubscriptionClientSerializer
    queryset = SubscriptionClient.objects.all()

    def create(self, request, *args, **kwargs):
        client_id = request.data['client_id']
        instance = Client.objects.filter(id=client_id).first()
        print(client_id,instance,request.data)
        if instance:
            instance.bonus += 10
            instance.save()

        return super().create(request, *args, **kwargs)


    def get_queryset(self):
      
        return SubscriptionClient.objects.filter(end_subscribe=timezone.now().date())
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
     
        if instance.end_subscribe <= timezone.now().date():
            return Response({"detail": "L'abonnement a expiré."}, status=404)
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)




class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()



class CalenderViewset(viewsets.ModelViewSet):

    serializer_class = CalenderSerailizers
    queryset = calender.objects.all()





