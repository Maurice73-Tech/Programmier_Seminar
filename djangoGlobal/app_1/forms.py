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