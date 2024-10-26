from django.urls import path,include
from .views import *
from rest_framework import routers
route = routers.SimpleRouter()

route.register('subscribe-admin',SubscriptionAdminViewSet,basename='admin')
route.register('subscribe-client',SubscriptionClientViewSet,basename='client')
route.register('collection',CollectionViewSet,basename = 'collection')
route.register('calender',CalenderViewset,basename='calender')
# route.register('modele',ModeleViewSet,basename='modele')
# route.register('voiture',VoitureViewSet ,basename='voiture')

urlpatterns =[
    path('',include(route.urls)),
    # path('search-marqueModele/<id>/', SearchModeleMarque.as_view(), name='read_marque'),

]