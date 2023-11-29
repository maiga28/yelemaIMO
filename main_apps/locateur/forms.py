from django import forms

CHOIX_SURFACE = [
    ('actif', 'Actif'),
    ('pas_actif', 'Pas_actif'),
    # ... autres options ...
]

class LocateurForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    prenom = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    tell = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    statut = forms.ChoiceField(choices=CHOIX_SURFACE, widget=forms.Select(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))

class Signaler_panneForm(forms.Form):
    titre = forms.CharField(widget=forms.Textarea(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    locateur = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))