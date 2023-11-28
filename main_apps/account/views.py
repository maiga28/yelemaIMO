
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignUpForm
from main_apps.account.models import Admiuser
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Admiuser


from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProfileUpdateForm

# Create your views here.
from django.shortcuts import render
from .models import Admiuser as User

@login_required
def profile_view(request,pk):
    user = get_object_or_404(User,pk=pk)
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


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("gestion:home")
            else:
                msg = 'Identifiants invalides'
        else:
            msg = 'Données du formulaire non valides. Veuillez vérifier vos saisies.'

    return render(request, "account/login.html", {"form": form, "msg": msg})

from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token



def register(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            
            user = Admiuser.objects.create_user(username=email, email=email, password=password)
            
            token = account_activation_token.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            verification_link = f"http://votre_site.com/verification/{uid}/{token}/"

            subject = 'Veuillez vérifier votre adresse e-mail'
            message = render_to_string('account/email_verification.html', {
                'user': user,
                'verification_link': verification_link,
            })
            user.email_user(subject, message)
            
            msg = 'User created successfully.'
            success = True
            return redirect('account:login')  # Redirect the user to the login page after registration

    else:
        form = SignUpForm()

    return render(request, "account/signup.html", {"form": form, "msg": msg, "success": success})

# account/views.py

from django.utils.encoding import force_str
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Admiuser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Admiuser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # Si le token est valide, marquez l'e-mail comme vérifié dans votre modèle utilisateur personnalisé
        user.is_email_verified = True
        user.save()
        # Vous pouvez effectuer d'autres opérations ou redirections ici en fonction de votre logique métier
        return render(request, 'account/verification_success.html')
    else:
        return render(request, 'account/verification_fail.html')




def logout_view(request):
    logout(request)
    return redirect('account:login')
