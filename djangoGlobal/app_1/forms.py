from django.contrib.auth import get_user_model
from django.forms.fields import ImageField
from .models import NeueBenutzer, Post, Kommentar,UnterKommentar
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django import forms
from django.contrib.auth import authenticate
from django.forms.widgets import NumberInput, Widget

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
        fields = ('kommentar', )

    
    name: forms.HiddenInput() 
    kommentar = forms.CharField (widget=forms.Textarea(attrs={'class':'form-control'}), label="Kommentar")

        
class UnterKommentarForm(forms.ModelForm) :
    
    name: forms.HiddenInput()
    unterkommentar=forms.CharField (widget=forms.Textarea(attrs={'class':'form-control'}), label="Unterkommentar")

    class Meta:
        model=UnterKommentar
        fields=('unterkommentar', )

class Profile_edit_form(UserChangeForm):
    username = forms.CharField (widget=forms.TextInput (attrs={'class':'form-control'}), label="Username")
    vorname = forms.CharField (widget=forms.TextInput (attrs={'class':'form-control'}), label="Vorname")
    nachname = forms.CharField (widget=forms.TextInput (attrs={'class':'form-control'}), label="Nachname")
    email = forms.EmailField (widget=forms.EmailInput (attrs={'class':'form-control'}), label="Email")
    abteilung = forms.CharField (widget=forms.TextInput ( attrs={'class':'form-control'}), label="Abteilung")
    geburtsdatum= forms.DateField(widget=forms.NumberInput (attrs={'class':'form-control', 'type':'date'}), label="Geburtsdatum")
    profile_pic = forms.ImageField(widget=forms.FileInput ( attrs={'class':'form-control'}),required=False)

    class Meta:
        model= NeueBenutzer
        fields = ('username','vorname', 'nachname','email','abteilung', 'geburtsdatum', 'profile_pic')


class Password_change_form(PasswordChangeForm):
    old_password = forms.CharField (widget=forms.PasswordInput (attrs={'class':'form-control'}), label="Altes Passwort")
    new_password1 = forms.CharField (widget=forms.PasswordInput (attrs={'class':'form-control'}), label="Neues Passwort")
    new_password2 = forms.CharField (widget=forms.PasswordInput (attrs={'class':'form-control'}), label="Neues Passwort wiederholen")
   
    

    class Meta:
        model= NeueBenutzer
        fields = ('old_password','new_password1', 'new_password2')
