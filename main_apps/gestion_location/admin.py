from django.contrib import admin
from .models import Employe


@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('name', 'prenom', 'poste', 'tell', 'email', 'domicile', 'date_of_birth', 'created_at', 'updated_at')
    list_filter = ('name', 'prenom', 'poste', 'tell', 'email', 'domicile', 'date_of_birth', 'created_at', 'updated_at')
    search_fields = ('name', 'prenom', 'poste', 'tell', 'email')
    list_per_page = 20


