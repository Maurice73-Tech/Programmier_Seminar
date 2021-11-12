from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import RequestContext, context
from .forms import Registrierungsform

# Dynamische dummy daten die ich so in die html abrufen kann
""" post =[
    {
        'author': 'Phillip Kunze',
        'title': 'Blog Post 1',
        'content': 'Wieder mal ein dummer eintrag eines dummen users',
        
    },
    {
        'author': 'Andy wandnageln',
        'title': 'Blog Post 2',
        'content': 'Wieder mal ein wilder beitrag',      
    }
] """

#beispielfunktion wie daten über ein dictionary zur html kommen

""" def index(request):
    context={'posts':post}
    return render(request, 'app_1/index.html', context) """


def impressum(request):
    return render(request,'impressum.html')

def home(request):
    return render(request, 'login_beratung.html')

def login(request):
    return render(request,'app_1/login_beratung.html')

def registrieren(request):
    form = Registrierungsform()

    if request.method == 'POST':
        form = Registrierungsform(request.POST)
        print('Post Request wurder erkannt')
        print(form.fields)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request, 'login.html', context)

def forum(request):
    return render(request,'forum.html')

def registrierung_sicht(request):
    if request.method == 'POST':
        signform= Registrierungsform(request.POST)
        if signform.is_valid():
            signform.save()

    else:
        signform=Registrierungsform()

    context= {
        'signform_schlüssel': signform
    }
    return render (request, 'login.html', context)

    #probieren