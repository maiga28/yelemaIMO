from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.list_client, name='client'),
    # Ajoutez d'autres modèles d'URL au besoin
]
