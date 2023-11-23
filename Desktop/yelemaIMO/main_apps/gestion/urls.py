from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
    
    path('', views.home, name='home'),
    path('list_users/', views.list_users, name='users'),
    path('ajouter_proprietaire/', views.ajouter_proprietaire, name='ajouter_proprietaire'),
    path('update_proprietaire/<int:proprietaire_id>/', views.update_proprietaire, name='update_proprietaire'),
    path('supprimer_proprietaire/<int:proprietaire_id>/', views.supprimer_proprietaire, name='supprimer_proprietaire'),
    path('ajouter_propriete/', views.ajouter_propriete, name='ajouter_propriete'),
    path('update_propriete/<int:propriete_id>/', views.update_propriete, name='update_propriete'),
    path('supprimer_propriete/<int:propriete_id>/', views.supprimer_propriete, name='supprimer_propriete'),
    path('details_list/<int:propriete_id>/', views.details_list, name='details_list'),
    
    
#    path('delete_user/<int:user_id>/', views.delete_profile, name='delete_profile'),
]
