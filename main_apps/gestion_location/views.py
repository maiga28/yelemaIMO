from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, get_object_or_404

from main_apps.gestion_location.models import Employe
from main_apps.client.models import Client
from main_apps.gestion.models import Proprietaire
from main_apps.gestion.models import Propriete
from main_apps.locateur.models import Locateur
from main_apps.account.models import Admiuser

from .forms import EmployeForm

# Create your views here.
def gestion_location(request):
    
    employers = Employe.objects.all()
    
        # Initialiser les listes à vide
    locateur_list = []
    proprietaire_list = []
    propriete_list = []
    client_list = []
    
    # Vérifier le rôle de l'utilisateur connecté
    if request.user.role == 'employe':
    
        locateur_list = Locateur.objects.all()
        proprietaire_list = Proprietaire.objects.all()
        propriete_list = Propriete.objects.all()
        client_list = Client.objects.all()
    
    context = {
        
        'employers': employers,
        'locateurs': locateur_list,
        'proprietaires': proprietaire_list,
        'proprietes': propriete_list,
        'clients': client_list
    }
    
    return render(request,'gestion_location/gestion_location.html',context)



from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from .forms import EmployeForm
from .models import Employe

def ajouter_employer(request):
    msg = None
    success = False
    
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            prenom = form.cleaned_data['prenom']
            poste = form.cleaned_data['poste']
            domicile = form.cleaned_data['domicile']
            tell = form.cleaned_data['tell']
            adresse = form.cleaned_data['adresse']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Crée un utilisateur Django
            user, created = Admiuser.objects.get_or_create(username=email, email=email)
            if created:
                user.set_password(password)
                user.save()
            
            # Crée un employé lié à l'utilisateur
            employer, created = Employe.objects.get_or_create(
                user=user,
                defaults={
                    'name': name,
                    'prenom': prenom,
                    'poste': poste,
                    'domicile': domicile,
                    'tell': tell,
                    'adresse': adresse,
                    'email': email,
                }
            )
            
            # Authentifie l'utilisateur nouvellement créé
            employer = authenticate(username=email, password=password)
            if employer is not None:
                login(request, employer)

            msg = 'User created successfully.'
            success = True
            return redirect('gestion_location:gestion_location')
    else:
        form = EmployeForm()

    return render(request, 'gestion_location/ajouter_employer.html', {'form': form, 'msg': msg, 'success': success})

def update_employer(request,pk):
    employer = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        form = EmployeForm(request.POST, isinstance=employer)
        if form.is_valid():
            form.save()
            return redirect('gestion_location:gestion_location')
    else:
        form = EmployeForm()
    return render(request, 'gestion_location/update_employer.html',{'form':form})   

def supprimer_employer(request,pk):
    employer = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        employer.delete()
        return redirect('gestion_location:gestion_location')
    return render(request, 'gestion_location/supprimer_employer',{'employer':employer})


@user_passes_test(lambda u: u.is_staff and hasattr(u, 'employer'))
def gestion_employer(request):
    employer = Employe.objects.all()
    
    return render(request,'gestion_location/employer.html')