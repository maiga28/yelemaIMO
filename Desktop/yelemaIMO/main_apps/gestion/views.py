from django.shortcuts import redirect, render
from .models import Proprietaire,Propriete,Caracteristique
from main_apps.gestion.forms import ProprieteForm,ProfileUpdateForm,ProprietaireForm

# Create your views here.
def home(request):
    proprietaires = Proprietaire.objects.all()
    proprietes = Propriete.objects.all()
    total_proprietaires = Proprietaire.objects.count()
    
    context = {
       'proprietaires': proprietaires,
       'proprietes': proprietes,
       'total_proprietaires': total_proprietaires,
    }

    return render(request, 'gestion/home.html', context)
################################### update # profile ####################################

from .forms import ProprietaireForm

def ajouter_proprietaire(request):
    if request.method == "POST":
        form = ProprietaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion:home')
    else:
        form = ProprietaireForm()
    proprietaires = Proprietaire.objects.all()
    proprietes = Propriete.objects.all()
    total_proprietaires = Proprietaire.objects.count()
    
    context = {
       'proprietaires': proprietaires,
       'proprietes': proprietes,
       'total_proprietaires': total_proprietaires,
       'form': form,
    }

    return render(request, 'gestion/home.html', context)

            
        

################################### update # profile ####################################

def update_proprietaire(request,proprietaire_id):
    form = Proprietaire.objects.get(id=proprietaire_id)
    if request.method == 'POST':
        form = ProprietaireForm(request.POST, request.FILE, isinstance=Proprietaire)
        if form.is_valid():
            form.save()
        else:
            form = ProprietaireForm(isinstance=Proprietaire)
    return render(request,'gestion/uptade_proprietaire.html', context={'form':form})