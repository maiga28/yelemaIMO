from django.urls import path
from . import views

app_name = 'gestion_location'

urlpatterns = [
    
    path('', views.gestion_location, name='gestion_location'),
    path('ajouter_employer/',views.ajouter_employer, name='ajouter_employer'),
    path('gestion_location/',views.gestion_location, name='gestion_location'),
    path('update_employer/<int:pk>/',views.update_employer, name='update_employer'),
    path('supprimer_employer/<int:pk>/',views.supprimer_employer, name='supprimer_employer')
    ]
# dashoboard_locateur