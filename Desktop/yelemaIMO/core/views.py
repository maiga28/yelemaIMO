from django.shortcuts import render
from main_apps.client.models import Client,Reservation
from main_apps.gestion.models import Proprietaire,Propriete

def index(request):
    proprietes = Propriete.objects.all()
    proprietaires = Proprietaire.objects.all()
    context = {
        'proprietes':proprietes,
        'proprietaires':proprietaires
    }
    return render(request, 'index.html',context)

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')