from django.shortcuts import render
from .models import Proprietaire,Propriete,Caracteristique
from .forms import ProprieteForm,ProfileUpdateForm,ProprietaireFrom

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
def ajouter_proprietaire(request):
    if request.method == "POST":
        form = ProprietaireFrom(request.POST, request.FILE, isinstance=Proprietaire)
        if form.is_valid():
            form.save()
        else:
            form = ProprietaireFrom(isinstance=Proprietaire)
    return render(request,'gestion/ajouter_proprietaire.html')
            
        

################################### update # profile ####################################

def update_proprietaire(request,proprietaire_id):
    form = Proprietaire.objects.get(id=proprietaire_id)
    if request.method == 'POST':
        form = ProprietaireFrom(request.POST, request.FILE, isinstance=Proprietaire)
        if form.is_valid():
            form.save()
        else:
            form = ProprietaireFrom(isinstance=Proprietaire)
    return render(request,'gestion/uptade_proprietaire.html', context={'form':form})