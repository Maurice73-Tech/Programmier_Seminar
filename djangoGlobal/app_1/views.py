from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import RequestContext, context
from .models import Post
from .forms import Registrierungsform
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
User = get_user_model()


Post =[
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
] 

#beispielfunktion wie daten über ein dictionary zur html kommen

""" def index(request):
    context={'posts':post}
    return render(request, 'app_1/index.html', context) """

class ForumView (ListView):
    model = Post
    template_name = 'forum.html'

def impressum(request):
    return render(request,'impressum.html')

def home(request):
    return render(request, 'login_beratung.html')

def forum(request):
    return render(request,'forum.html')

def login(request):
    return render(request,'app_1/login_beratung.html')

def registrieren(request):
    form = Registrierungsform()

    if request.method == 'POST':
        form = Registrierungsform(request.POST)
        print('Post Request wurder erkannt')
        if form.is_valid():
            form.save()
            return redirect ('/login2')

    context={'form':form}
    return render(request, 'registrieren.html', context)

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
    return render (request, 'login.html', context)

@login_required (login_url= 'login2.html')
def profile (request):
    return render(request, 'profile.html')