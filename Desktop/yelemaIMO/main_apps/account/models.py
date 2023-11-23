import datetime
from django.db import models
from django.contrib.auth.models import User
from dateutil.parser import parse as parse_datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=30)
    image = models.ImageField(upload_to='image/')
    bio = models.TextField(max_length=500, blank=True)
    telephone = models.CharField(max_length=20)
    location = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    def formatted_registration_date(self):
        return parse_datetime(str(self.user.date_joined))

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return super(Profile, self).save(*args, **kwargs)