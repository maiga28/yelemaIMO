
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User

from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProfileUpdateForm

# Create your views here.
from django.shortcuts import render
from .models import Profile as UserProfile

@login_required
def profile_view(request,pk):
    user = get_object_or_404(UserProfile,pk=pk)
    context = {
        'user':user
        } 
    return render(request, 'account/user_profile.html', context)
######################################     une vue de mise à jour de profil et un formulaire de modification de profil.   ###############################################################
@login_required
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_view')

    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, 'account/update_user.html', {'form': form})

@login_required
def delete_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('account:profile_view')
    else:
        user = User
    return render(request, 'account/delete_user.html', {'user':user})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Vérifiez si l'utilisateur existe déjà
            try:
                user = User.objects.get(username=email)
                msg = "L'utilisateur avec cet e-mail existe déjà."
            except User.DoesNotExist:
                # L'utilisateur n'existe pas, vous pouvez créer un nouvel utilisateur
                user = User.objects.create_user(email, email, password)
                msg = "L'utilisateur a été enregistré avec succès."

            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("gestion:home")
            else:
                msg = 'Identifiants invalides'
        else:
            msg = 'Données du formulaire non valides. Veuillez vérifier vos saisies.'

    return render(request, "account/login.html", {"form": form, "msg": msg})




def register(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(email, email, password)
            
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)

            msg = 'User created successfully.'
            success = True
            return redirect('account:login')  # Redirect the user to the login page after registration

    else:
        form = SignUpForm()

    return render(request, "account/signup.html", {"form": form, "msg": msg, "success": success})

def logout_view(request):
    logout(request)
    return redirect('account:login')
