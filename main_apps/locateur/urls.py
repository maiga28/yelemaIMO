from django.urls import path
from . import views

app_name = 'locateur'

urlpatterns = [
        
        path('',views.gestion_locateur, name='gestion_locateur'),
        path('ajouter_locateur/',views.ajouter_locateur, name='ajouter_locateur'),
        path('lien_conf/',views.lien_conf, name='lien_conf'),
    
    ]
