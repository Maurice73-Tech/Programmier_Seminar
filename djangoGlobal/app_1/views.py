from django.http import request 
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import AddBlogForm, Registrierungsform, Anmeldeform
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView
from .models import NeueBenutzer, Post

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

def benutzerübergabe (request):
    
    context = {}
    accounts= NeueBenutzer.objects.all()
    context ['accounts'] = accounts
    
    return render(request, "forum.html", context)

def impressum(request):
    return render(request,'impressum.html')


def registrieren(request):
    context = {}

    if request.POST:
        form = Registrierungsform(request.POST)
        print('Post Request wurder erkannt')
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get ('username')
            raw_password=form.cleaned_data.get ('password1')
            account = authenticate (username=username, password=raw_password)
            login (request, account)
            return redirect ('forum')
        else:
            context ['registrierungs_form']=form
    else:
        form = Registrierungsform ()
        context ['registrierungs_form'] = form

    return render(request, 'registrieren.html', context)

def forum(request):
    return render(request,'forum.html')


def benutzer_login(request):
    if request.method == 'POST':
        form = Registrierungsform(request.POST)
        username= request.POST['username']
        password= request.POST ['password']
        user = authenticate(username= username, password= password)
        print ('Komme bis hier1')
    
        if user:
            login (request, user)
            messages.info(request, ('Sie sind jetzt angemeldet'))
            redirect('/forum')
            print ('Komme bis hier2')
        else:
            messages.info (request,'Username oder Passwort ist nicht korrekt!')

    context= {}
    return render (request, 'login.html', context)

def benutzer_logout(request):
    logout(request)
    return redirect ('/login')
    print ('Erfolgreich abgemeldet!')


def profile (request):
    return render(request, 'profile.html')

def add_block_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect ('authentifizieren')
    form = AddBlogForm (request.POST or None)
    if form.is_valid():
        obj = form.save (commit=False)
        Autor = NeueBenutzer.objects.filter(username =user.username).first()
        obj.Autor = Autor
        obj.save ()
        form = Post()
        return redirect ('forum')

    context ['form'] = form

    return render (request, 'addpost.html', context)     

def authentifizieren_view (request):
    return render (request, 'authentifizieren.html', {})

        

