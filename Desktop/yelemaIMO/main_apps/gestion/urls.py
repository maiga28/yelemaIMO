from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
    
    path('', views.home, name='home'),
    path('', views.ajouter_proprietaire, name='ajouter_proprietaire'),
    path('update_proprietaire/<int:proprietaire_id>/', views.update_proprietaire, name='update_proprietaire'),
    
#    path('delete_user/<int:user_id>/', views.delete_profile, name='delete_profile'),
]
