from django.db import models
from main_apps.gestion.models import Propriete, Contrat_bail

# Create your models here.

class Locateur(models.Model):
    name = models.CharField(max_length=30,blank=False,null=False)
    prenom = models.CharField(max_length=30,blank=False,null=False)
    tell = models.IntegerField(blank=False,null=False)
    email = models.EmailField(max_length=30,blank=False,null=False)
    statut = models.CharField(max_length=20, choices=[('actif', 'Actif'),('pas_actif', 'Pas_actif')])
    propriete = models.OneToOneField(Propriete, on_delete=models.CASCADE,blank=False,null=False)
   # contrat = models.OneToOneField(Propriete, on_delete=models.CASCADE,blank=False,null=False)
    email_confirmed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    
class Signaler_panne(models.Model):
    titre = models.TextField(max_length=500,blank=False,null=False)
    locateur = models.OneToOneField(Locateur, on_delete=models.CASCADE, related_name='signaler_une_panne')
    