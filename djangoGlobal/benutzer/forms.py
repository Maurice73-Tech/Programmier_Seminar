from django.contrib.auth.models import User
from django.forms import fields
import forms

class Registrierungsform(forms.ModelForm):
    class Meta:
        model= User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']