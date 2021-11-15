from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import RequestContext, context
from .forms import Registrierungsform
from django.contrib.auth import authenticate, login, logout, get_user_model
User = get_user_model()

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
        if form.is_valid():
            form.save()
            return redirect ('/login')

    context={'form':form}
    return render(request, 'login.html', context)

def forum(request):
    return render(request,'forum.html')

#noch fixen funktioniert noch nicht POST Methode klappt nicht, bzw holt die Daten nicht
def login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
    
    user = authenticate(request, username= username, password= password)
    
    if user is not None:
        login (request, user)
        return redirect('/impressum')

    context= {}
    return render (request, 'login_beratung.html', context)

    #probieren