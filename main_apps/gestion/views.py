from django.shortcuts import redirect, render
from .models import Proprietaire,Propriete
from main_apps.gestion.forms import ProprieteForm,ProprietaireForm
from django.core.paginator import Paginator

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Proprietaire, Propriete
from main_apps.client.models import Client,Reservation

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    proprietes = Propriete.objects.all()
    proprietaires = Proprietaire.objects.all()
    total_proprietaires = Proprietaire.objects.count()
    total_proprietes = Propriete.objects.count()
    total_client = Client.objects.count()
    total_reservation = Reservation.objects.count()

    paginator = Paginator(proprietaires, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'proprietes':proprietes,
        'proprietaires': page_obj,  # Utilisez page_obj au lieu de proprietaires ici
        'total_proprietaires': total_proprietaires,
        'total_proprietes':total_proprietes,
        'page_obj': page_obj,
        'total_client':total_client,
        'total_reservation':total_reservation
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

    

from django.shortcuts import render, redirect
from .forms import ProprieteForm
from .models import Propriete

def ajouter_propriete(request):
    if request.method == 'POST':    
        form = ProprieteForm(request.POST)
        if form.is_valid():
            # Créez une nouvelle instance du modèle Propriete avec les données du formulaire        
            titre = form.cleaned_data['titre']
            adresse = form.cleaned_data['adresse']
            description = form.cleaned_data['description']
            prix = form.cleaned_data['prix']
            proprietaire = form.cleaned_data['proprietaire']
            statut = form.cleaned_data['statut']
            type_propriete = form.cleaned_data['type_propriete']
            nombre_chambres = form.cleaned_data['nombre_chambres']
            nombre_salles_bains = form.cleaned_data['nombre_salles_bains']
            surface_m2 = form.cleaned_data['surface_m2']

            # Enregistrez la nouvelle propriété dans la base de données
            try:
                propriete = Propriete.objects.create(
                    titre=titre,
                    adresse=adresse,
                    description=description,
                    prix=prix,
                    proprietaire=proprietaire,
                    statut=statut,
                    type_propriete=type_propriete,
                    nombre_chambres=nombre_chambres,
                    nombre_salles_bains=nombre_salles_bains,
                    surface_m2=surface_m2
                )
                return redirect('gestion:home')
            except Exception as e:
                print("Erreur lors de l'enregistrement de la propriété :", e)
                # Vous pouvez ajouter d'autres messages de débogage si nécessaire
        else:
            print("Formulaire invalide :", form.errors)
    else:
        form = ProprieteForm()

    context = {'form': form}
    return render(request, 'gestion/ajouter_propriete.html', context)
################################ Update propriete ##################################################################
def update_propriete(request, propriete_id):
    propriete = get_object_or_404(Propriete, id=propriete_id)
    
    if request.method == 'POST':
        form = ProprieteForm(request.POST, instance=propriete)
        if form.is_valid():
            form.save()
            return redirect('gestion:home')  # Rediriger vers la page d'accueil après la mise à jour
    else:
        form = ProprieteForm()  # Remplir le formulaire avec les données existantes

    return render(request, 'gestion/update_propriete.html', context={'form': form})

def supprimer_propriete(request, propriete_id):
    propriete = get_object_or_404(Propriete, id=propriete_id)
    
    if request.method == 'POST':
        propriete.delete()
        return redirect('gestion:home')  # Rediriger vers la page d'accueil après la suppression
    
    return render(request, 'gestion/supprimer_propriete.html', context={'propriete': propriete})


def details_list(request, propriete_id):
    propriete = get_object_or_404(Propriete, id=propriete_id)
    return render(request, 'gestion/details_list.html', {'propriete': propriete})

def list_users(request):
    return render(request,'gestion/list_users.html')