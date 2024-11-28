from django import forms
from .models import Language, User, Exchange

# Forma za unos novog jezika
class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Unesite naziv jezika'}),
        }

# Forma za unos novog korisnika
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Unesite korisničko ime'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Unesite email'}),
        }

# Forma za unos nove razmjene jezika
class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = ['language', 'user']
        widgets = {
            'language': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }
