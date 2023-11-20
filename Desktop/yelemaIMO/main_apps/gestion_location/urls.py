from django.urls import path
from . import views

app_name = 'gestion_location'

urlpatterns = [
    
    path('', views.gestion_location, name='gestion_location'),
    
    ]
# dashoboard_locateur