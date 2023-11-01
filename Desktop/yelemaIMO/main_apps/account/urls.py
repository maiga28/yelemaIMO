from django.urls import path
from . import views

app_name = 'account'  # Nom de votre espace de noms

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    # Autres patterns d'URL au besoin
]
