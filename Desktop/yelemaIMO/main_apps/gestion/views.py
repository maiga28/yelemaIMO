from django.shortcuts import redirect, render
from .models import Proprietaire,Propriete,Caracteristique
from main_apps.gestion.forms import ProprieteForm,ProprietaireForm
from django.core.paginator import Paginator

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Proprietaire, Propriete

def home(request):
    proprietaires = Proprietaire.objects.all()
    total_proprietaires = Proprietaire.objects.count()

    paginator = Paginator(proprietaires, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'proprietaires': page_obj,  # Utilisez page_obj au lieu de proprietaires ici
        'total_proprietaires': total_proprietaires,
        'page_obj': page_obj
    }

    return render(request, 'gestion/home.html', context)


################################### update # profile ####################################

from .forms import ProprietaireForm

from django.shortcuts import redirect, render
from .forms import ProprietaireForm
from .models import Proprietaire

def ajouter_proprietaire(request):
    if request.method == "POST":
        form = ProprietaireForm(request.POST)
        if form.is_valid():
            # Récupérez les données du formulaire
            name = form.cleaned_data['name']
            s_name = form.cleaned_data['s_name']
            numero_telephone = form.cleaned_data['numero_telephone']
            adresse = form.cleaned_data['adresse']
            email = form.cleaned_data['email']
            
            # Recherchez si un Proprietaire avec la même adresse e-mail existe déjà
            proprietaire, created = Proprietaire.objects.get_or_create(email=email, defaults={
                'name': name,
                's_name': s_name,
                'adresse': adresse,
                'numero_telephone': numero_telephone
            })

            return redirect('gestion:home')
    else:
        form = ProprietaireForm()

    context = {'form': form}
    return render(request, 'gestion/ajouter_proprietaire.html', context)


            
        

################################### update # profile ####################################

from django.shortcuts import render, get_object_or_404
from .forms import ProprietaireForm
from .models import Proprietaire

def update_proprietaire(request, proprietaire_id):
    proprietaire = get_object_or_404(Proprietaire, id=proprietaire_id)
    
    if request.method == 'POST':
        form = ProprietaireForm(request.POST, instance=proprietaire)
        if form.is_valid():
            form.save()
            return redirect('gestion:home')  # Rediriger vers la page d'accueil après la mise à jour
    else:
        form = ProprietaireForm()  # Remplir le formulaire avec les données existantes

    return render(request, 'gestion/update_proprietaire.html', context={'form': form})


def supprimer_proprietaire(request, proprietaire_id):
    proprietaire = get_object_or_404(Proprietaire, id=proprietaire_id)
    
    if request.method == 'POST':
        proprietaire.delete()
        return redirect('gestion:home')  # Rediriger vers la page d'accueil après la suppression
    
    return render(request, 'gestion/supprimer_proprietaire.html', context={'proprietaire': proprietaire})


    
