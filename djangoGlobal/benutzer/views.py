from django.shortcuts import render
from .forms import SignupForm

def registrierung_sicht(request):
    if request.method == 'POST':
        signform= SignupForm(request.POST)
        if signform.is_valid():
            signform.save()

    else:
        signform=SignupForm()

    context= {
        'signform_schlüssel': signform
    }
    return render (request, 'benutzer/registrierung.html', context)
