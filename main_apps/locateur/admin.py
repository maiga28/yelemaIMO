from django.contrib import admin

# Register your models here.
from .models import Locateur, Signaler_panne

@admin.register(Locateur)
class LocateurreAdmin(admin.ModelAdmin):
    list_display = ('name', 'prenom', 'tell', 'statut', 'email')
    list_filter = ('name','prenom','email')
    
    
@admin.register(Signaler_panne)
class Signaler_panneAdmin(admin.ModelAdmin):
    list_display = ('titre', 'locateur')
    list_filter = ('titre', 'locateur')
    search_fields = ('titre', 'locateur')
    list_per_page = 20


