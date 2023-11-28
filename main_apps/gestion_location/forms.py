from django import forms
from .models import Employe



from django import forms


    
from django import forms
from django.contrib.auth.models import User
from .models import Employe

class EmployeForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    prenom = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    poste = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    domicile = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    tell = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    adresse = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))

    def save(self):
        # Crée l'utilisateur Django
        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )

        # Crée l'employé et le lie à l'utilisateur
        employe = Employe.objects.create(
            name=self.cleaned_data['name'],
            prenom=self.cleaned_data['prenom'],
            poste=self.cleaned_data['poste'],
            domicile=self.cleaned_data['domicile'],
            tell=self.cleaned_data['tell'],
            adresse=self.cleaned_data['adresse'],
            email=self.cleaned_data['email'],
            user=user
        )
        return employe


