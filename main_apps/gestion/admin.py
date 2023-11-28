from django.contrib import admin
from .models import Proprietaire, Propriete

# Register your models here.
@admin.register(Proprietaire)
class ProprietaireAdmin(admin.ModelAdmin):
    list_display = ('name', 's_name', 'adresse', 'numero_telephone', 'email')

@admin.register(Propriete)
class ProprieteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'adresse', 'prix', 'proprietaire', 'statut', 'type_propriete', 'nombre_chambres', 'nombre_salles_bains', 'surface_m2')
    list_filter = ('statut', 'type_propriete')
    search_fields = ('titre', 'adresse', 'prix', 'proprietaire__name', 'proprietaire__s_name')
    list_per_page = 20


