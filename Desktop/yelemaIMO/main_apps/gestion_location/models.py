from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer')
    name = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    poste = models.CharField(max_length=30, unique=True)
    adresse = models.CharField(max_length=30, unique=True)
    tell = models.IntegerField()
    email = models.EmailField(unique=True)
    domicile = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=30,unique=True,blank=False,null=False)
    
    def __str__(self):
        return self.name