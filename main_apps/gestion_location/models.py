from django.conf import settings
from django.contrib.auth.models import Permission
from django.db import models
from django.contrib.contenttypes.models import ContentType
from main_apps.account.models import Admiuser
from main_apps.locateur.models import Locateur

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from dateutil.parser import parse as parse_datetime

class Employe(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employes_user')
    name = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')
    poste = models.CharField(max_length=255, unique=True, blank=False)
    domicile = models.CharField(max_length=255)
    tell = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    user_auth = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employe_user_auth')
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def can_CRUD_locateur(self):
        # Vérifie si l'Employe a la permission de CRUD sur le modèle Locateur
        content_type = ContentType.objects.get_for_model(Locateur)  # Assurez-vous de remplacer 'Locateur' par le vrai nom de votre modèle
        permission_codename = 'can_CRUD_locateur'
        return self.user_auth.has_perm(permission_codename, content_type)
