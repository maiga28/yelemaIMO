from django.urls import path
from . import views

app_name = 'account'  # Nom de votre espace de noms

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),
    path('update_user/<int:pk>/', views.update_user, name='update_user'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('verification/<str:uidb64>/<str:token>/', views.send_verification_email, name='email_verification'),
    # Autres patterns d'URL au besoin
]
