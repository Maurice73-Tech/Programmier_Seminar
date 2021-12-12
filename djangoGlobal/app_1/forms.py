from django.contrib.auth import get_user_model
from .models import NeueBenutzer, Post, Kommentar, UnterKommentar
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.contrib.auth import authenticate

class Registrierungsform(UserCreationForm):
    vorname = forms.CharField (label="Vorname")
    nachname = forms.CharField (label="Nachname")
    abteilung = forms.CharField (label="Abteilung")
    geburtsdatum= forms.DateField(label="Geburtsdatum")
    email = forms.EmailField (max_length=50, label='E-Mail', help_text='Erforderlich- Bitte geben Sie eine gültige E-Mail ein!')

    class Meta:
        model= NeueBenutzer
        fields = ('vorname', 'nachname','abteilung','username', 'geburtsdatum', 'email', 'password1', 'password2')

        

class Anmeldeform (forms.ModelForm):
    password = forms.CharField (label='Password', widget=forms.PasswordInput)

    class Meta:
        model = NeueBenutzer
        fields =('username', 'password')

    def clean (self):
        username = self.cleaned_data ('username')
        password = self.cleaned_data ('password')
        if not authenticate (username=username, password= password):
            raise forms.ValidationError ('Keine Anmeldung möglich!')
class AddBlogForm (forms.ModelForm):
    class Meta:
        model= Post
        fields = ['Titel', 'Inhalt']

class KommentarForm(forms.ModelForm):
    class Meta:
        model=Kommentar
        fields = ('name','content')
        

    widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'content': forms.Textarea(attrs={'class':'form-control'}),
    }
class UnterKommentarForm(KommentarForm) :
    model=UnterKommentar
    fields=('content')

    widgets={
        'body':forms.TextInput(attrs={'class':'form-control'})
    }

class Profile_edit_form(UserChangeForm):
    username = forms.CharField (label="Username")
    vorname = forms.CharField (label="Vorname")
    nachname = forms.CharField (label="Nachname")
    email = forms.EmailField (max_length=50, label='E-Mail')
    abteilung = forms.CharField (label="Abteilung")
    geburtsdatum= forms.DateField(label="Geburtsdatum")
    

    class Meta:
        model= NeueBenutzer
        fields = ('username','vorname', 'nachname','email','abteilung', 'geburtsdatum')