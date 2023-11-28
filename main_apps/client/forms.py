from django import forms
from . models import Client

class ClientForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))

class ClientUpdateForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
   
from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
   