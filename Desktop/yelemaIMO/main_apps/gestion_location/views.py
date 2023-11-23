from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, get_object_or_404
from main_apps.gestion_location.models import Employe
#from main_apps.locateur.models import Locateur

from .forms import EmployeForm

# Create your views here.
def gestion_location(request):
    employers = Employe.objects.all()
    # locateur_list = Locateur.objects.filter()
    # proprietaire_list = Proprietaire.objects.filter()
    # propriete_list = propriete.objects.filter()
    # client_list = Client.objects.filter()
    
    context = {
        'employers': employers
    }
    
    return render(request,'gestion_location/gestion_location.html',context)

from django.contrib.auth.models import User

def ajouter_employer(request):
    user = User
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
            user = form.cleaned_data['user']
            
          
            
            employer, created = Employe.objects.get_or_create(User)
            
            employer = authenticate(username=email, password=password)
            if employer is not None:
                login(request, employer)

            msg = 'User created successfully.'
            success = True
            return redirect('gestion_location:gestion_location')
    else:
        form = EmployeForm(isinstance=User)
    return render(request, 'gestion_location/ajouter_employer.html', {'form':form})

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