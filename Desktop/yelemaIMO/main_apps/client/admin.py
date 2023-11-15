from django.contrib import admin
from .models import Client
# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')
    list_per_page = 5