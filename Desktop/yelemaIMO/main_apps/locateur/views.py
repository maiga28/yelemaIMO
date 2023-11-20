from django.shortcuts import render

# Create your views here.
def locateur(request):
    return render(request,'locateur/locateur.html')
def login_locateur(request):
    return render(request,'locateur/login_locateur.html')