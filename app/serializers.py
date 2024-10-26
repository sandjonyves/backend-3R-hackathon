from rest_framework import serializers
from app.models import calender, Collection, SubscriptionAdmin, SubscriptionClient


class SubscriptionAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionAdmin
        fields = ['admin_id', 'start_subscribe', 'end_subscribe', 'status']
        # read_only_fields = ['end_subscribe', 'status']  

    def create(self, validated_data):
       
        return super().create(validated_data)
    
class SubscriptionClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionClient
        fields = ['admin_id', 'start_subscribe', 'end_subscribe', 'status','client_id']
        # read_only_fields = ['end_subscribe', 'status']  

    def create(self, validated_data):
       
        return super().create(validated_data)
    
class CollectionSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Collection
        fields = '__all__'  


class CalenderSerailizers(serializers.ModelSerializer):

    class Meta:
        model = calender
        fields = ('__all__')