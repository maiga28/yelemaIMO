from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from . models import Client
from main_apps.account.models import Admiuser

from main_apps.gestion.models import Propriete,Proprietaire
from . models import Reservation
from .forms import ReservationForm, ClientForm,ClientUpdateForm

# Create your views here.
def list_client(request):
    
    clients = Client.objects.all()
    context = {
        'clients':clients
    }
    
    return render(request, 'client/list_client.html',context)

def ajouter_client(request):
    if request.method == 'POST':    
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Enregistrez le nouveau client dans la base de données
            try:
                client = Client.objects.create(
                    name=name,
                    email=email,
                )
                return redirect('gestion:home')
            except Exception as e:
                print("Erreur lors de l'enregistrement de la propriété :", e)
                # Vous pouvez ajouter d'autres messages de débogage si nécessaire
        else:
            print("Formulaire invalide :", form.errors)
    else:
        form = ClientForm()

    context = {'form': form}
    return render(request, 'client/ajouter_client.html', context)


def update_client(request,client_id):
    client = get_object_or_404(Client,id=client_id)
    
    if request.method == 'POST':
        form = ClientUpdateForm(request.POST,  instance=client)
        if form.is_valid():
            form.save()
            return redirect('gestion:home') 
    else:
        form = ClientUpdateForm()  # Remplir le formulaire avec les données existantes

    return render(request, 'client/update_client.html', context={'form': form})

def supprimer_client(request):
    
    return render(request, 'client/supprimer_client.html')

from django.shortcuts import render, get_object_or_404, redirect


from .forms import ReservationForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import Propriete, Client, Reservation
from .forms import ReservationForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import Propriete, Reservation, Client
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required


def reservation(request, propriete_id):
    propriete = get_object_or_404(Propriete, pk=propriete_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Récupérez les informations du formulaire
            client, created = Client.objects.get_or_create(
                email=form.cleaned_data['email'],
                defaults={'name': form.cleaned_data['name']}
            )
           
            # Créez la réservation avec la propriété et le client
            try:
                reservation = Reservation.objects.create(
                    propriete=propriete,
                    client=client
                )
                
                # Mettez à jour le statut de la propriété
                propriete.statut = 'indisponible'
                propriete.save()

                return redirect('locateur:lien_conf')  # Redirige vers une page de confirmation de réservation
            except Exception as e:
                print("Erreur lors de l'enregistrement de la propriété :", e)
                # Vous pouvez ajouter d'autres messages de débogage si nécessaire
        else:
            print("Formulaire invalide :", form.errors)
            # Traitez le cas où le formulaire n'est pas valide, par exemple, en renvoyant le formulaire avec des erreurs

    else:
        form = ReservationForm()

    context = {
        'propriete': propriete,
        'form': form
    }

    return render(request, 'client/reservation.html', context)

