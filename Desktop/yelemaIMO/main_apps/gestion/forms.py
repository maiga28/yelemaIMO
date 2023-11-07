from django import forms
from .models import Proprietaire,Propriete,Caracteristique



from django import forms


    
class ProprietaireForm(forms.Form):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    s_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    numero_telephone = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    adresse = forms.CharField(widget=forms.TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}))
   


from django import forms
from .models import Propriete

class ProprieteForm(forms.ModelForm):
    class Meta:
        model = Propriete
        fields = ['titre', 'adresse', 'description', 'prix', 'proprietaire', 'statut', 'type_propriete', 'nombre_chambres', 'nombre_salles_bains', 'surface_m2']
        widgets = {
            'titre': forms.TextInput(
                attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}),
            'adresse': forms.TextInput(
                attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}),
            'description': forms.TextInput(
                attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}),
            'prix': forms.NumberInput(
                attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}),
            'proprietaire': forms.Select(
                attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}),
            'statut': forms.Select(
                attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}),
            'type_propriete': forms.Select(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}),
            'nombre_chambres': forms.NumberInput(
                attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}),
            'nombre_salles_bains': forms.NumberInput(
                attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}),
            'surface_m2': forms.NumberInput(
                attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'}),
        }
