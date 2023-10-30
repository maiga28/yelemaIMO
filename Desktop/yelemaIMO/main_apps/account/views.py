from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User


def login(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == 'POST':
        form = login(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("gestion:home")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "account/login.html", {"form": form, "msg": msg})


def register(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect('login')

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "account/register.html", {"form": form, "msg": msg, "success": success})

def logout(request):
    logout(request)
    return redirect('login')
