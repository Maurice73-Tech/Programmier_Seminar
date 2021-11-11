from django.contrib.auth.models import User
from django.forms import fields
from django import forms

class Registrierungsform(forms.ModelForm):
    class Meta:
        model= User
        fields = ('__all__')