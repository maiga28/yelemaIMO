from django.contrib import admin
from .models import Client,Reservation
# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'tell')
    list_filter = ('name', 'email', 'tell')
    search_fields = ('name', 'email', 'tell')
    list_per_page = 5
    

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('propriete', 'client')
    list_filter = ('propriete', 'client')
    search_fields = ('propriete', 'client')
    list_per_page = 5