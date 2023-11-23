from django.urls import path
from . import views

app_name = 'locateur'

urlpatterns = [
    
    path('',views.lien_conf, name='lien_conf'),
    
    ]
