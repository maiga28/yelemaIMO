from django.db import models
from main_apps.gestion.models import Propriete

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name



class Reservation(models.Model):
    propriete = models.ForeignKey(Propriete, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)