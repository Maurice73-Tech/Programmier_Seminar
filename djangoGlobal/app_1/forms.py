from django.contrib.auth.models import User
from django.forms import fields
from django import forms

class Registrierungsform(forms.ModelForm):
    vorname = forms.CharField (label="Vorname")
    nachname = forms.CharField (label="Nachname")
    abteilung = forms.CharField (label="Abteilung")
    geburtsdatum= forms.DateField(label="Geburtsdatum")
    #kommentar für commit2
    class Meta:
        model= User
        fields = ('vorname', 'nachname','abteilung','username', 'geburtsdatum', 'password',)

        widgets = {
            'vorname': forms.TextInput(attrs={'class': 'form-control'}),
            'nachname': forms.TextInput(attrs={'class': 'form-control'}),
            'abteilung': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'geburtsdatum': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'})
        }