import datetime
from django.conf import settings
from django.db import models
#from django.contrib.auth.models import User
from dateutil.parser import parse as parse_datetime
from django.contrib.auth.models import AbstractUser,AnonymousUser
#from main_apps.account.models import Admiuser
#from django.contrib.auth.models import User




ROLE_CHOICES = [
    
    
        ('client', 'Client'),
        ('employe', 'Employé'),
        # Ajoutez d'autres rôles au besoin
        
    ]

class Admiuser(AbstractUser):
    user = models.OneToOneField('self', on_delete=models.CASCADE, verbose_name="My Custom Field", null=True, blank=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    email_confirmed = models.BooleanField(default=False)
    email = models.EmailField(max_length=30)
    image = models.ImageField(upload_to='image/')
    bio = models.TextField(max_length=500, blank=True)
    telephone = models.CharField(max_length=20)
    location = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_email_verified(self):
        return self.email_confirmed

    
    def __str__(self):
        return self.username
    
    def formatted_registration_date(self):
        return parse_datetime(str(self.date_joined))

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        super().save(*args, **kwargs)


