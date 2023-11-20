from django.urls import path
from . import views

app_name = 'locateur'

urlpatterns = [
    
    path('', views.locateur, name='locateur'),
    path('login_locateur/',views.login_locateur, name='login_locateur'),
    
    ]
