from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import RequestContext, context
from .models import Post, NeueBenutzer
from .forms import Registrierungsform
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth import login as auth_login
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

class BlogDetailView (DetailView):
    model = Post
    template_name = 'blog-details.html'

def impressum(request):
    return render(request,'impressum.html')


def registrieren(request):
    form = Registrierungsform()

    if request.method == 'POST':
        form = Registrierungsform(request.POST)
        print('Post Request wurder erkannt')
        if form.is_valid():
            form.save()
            return redirect ('/forum')

    context={'form':form}
    return render(request, 'registrieren.html', context)

def forum(request):
    return render(request,'forum.html')


def benutzer_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username= username, password= password)
        print ('Komme bis hier1')
    
        if user is not None:
            login (request, NeueBenutzer)
            print ('Komme bis hier2')
            messages.success(request, ('Sie sind jetzt angemeldet'))
            redirect('/forum')
        else:
            messages.info (request,'Username oder Passwort ist nicht korrekt!')

    context= {}
    return render (request, 'login.html', context)


def profile (request):
    return render(request, 'profile.html')