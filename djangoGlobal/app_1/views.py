#Imports
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.db.models import fields
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from app_1.forms import AddBlogForm, Registrierungsform, KommentarForm,UnterKommentarForm, Post, Profile_edit_form, Password_change_form
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView
from app_1.models import NeueBenutzer, Kommentar, Post, UnterKommentar
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin

# Erstelle User werden übergeben
def benutzeruebergabe (request):
    context = {}
    accounts= NeueBenutzer.objects.all()
    context ['accounts'] = accounts
    
    return render(request, "forum.html", context)

# Methode um User zu registrieren
def registrieren(request):
    context = {}

    # Form wird geladen und Username + Passwort gesaved
    if request.POST:
        form = Registrierungsform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get ('username')
            raw_password=form.cleaned_data.get ('password1')
            account = authenticate (username=username, password=raw_password)
            login (request, account)
            return redirect ('forum')
       
        else:
            context ['registrierungs_form']=form
            messages.error(request,'Passwort oder Username ist falsch!')
    else:
        form = Registrierungsform ()
        context ['registrierungs_form'] = form

    return render(request, 'registrieren.html', context)    

# Methode um User einzuloggen
def benutzer_login(request):
    if request.method == 'POST':
        form = Registrierungsform(request.POST)
        username= request.POST['username']
        password= request.POST ['password']
        user = authenticate(username= username, password= password)
        
        # User wird eingeloggt
        if user:
            login (request, user)
            return redirect('/forum')
        
        else:
                messages.error(request,'Passwort oder Username ist falsch!')

    context= {}
    return render (request, 'login.html', context)

# Methode um User auszuloggen
def benutzer_logout(request):
    logout(request)
    messages.info(request, 'Sie wurden ausgeloggt, bis zum nächsten mal!')
    return redirect ('/login')

# Methode um bei nicht erfolgreicher Authentifikation auf die Authentifikationsseite weitergeleitet zu werden
def authentifizieren_view (request):
    return render (request, 'authentifizieren.html', {})

# Methode um Profil eines Users anzuzeigen
def profile (request):
    user=request.user
    if not user.is_authenticated:
        return redirect ('authentifizieren')    
    
    return render(request, 'profile.html')

# Klasse für das Editieren eines Userprofils   
class profile_edit (SuccessMessageMixin ,generic.UpdateView):
   form_class= Profile_edit_form 
   template_name = 'profile_edit.html'
   success_url = reverse_lazy ('profile')
   success_message = "Ihr Profil wurde geupdated!"

   def get_object (self):
       return self.request.user

# Klasse für das Ändern eines Passworts   
class Passwords_View (SuccessMessageMixin ,PasswordChangeView):
    form_class = Password_change_form
    success_url = reverse_lazy ('profile')
    success_message = "Ihr Passwort wurde geändert!"

class ForumView (ListView):
    model = Post
    template_name = 'forum.html'
    
class BlogDetailView (DetailView):
    model = Post
    template_name = 'blog-details.html'

class UpdateBlogView (UpdateView):
    model = Post
    template_name = 'update-blog.html'
    fields =['Titel','Inhalt']
    success_message = "Ihr Blogpost wurde geändert!"

def impressum(request):
    return render(request,'impressum.html')

# Methode für das Erstellen eines Blogposts   
def add_block_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect ('authentifizieren')
    form = AddBlogForm (request.POST or None)

    # Erster User und damit der eingeloggte User wird dem Attribut Autor übergeben
    if form.is_valid():
        obj = form.save (commit=False)
        Autor = NeueBenutzer.objects.filter(username =user.username).first()
        obj.Autor = Autor
        obj.save ()
        form = Post()
        messages.info(request, "Ihre Frage wurde erstellt!")
        return redirect ('forum')
        
    context ['form'] = form
    return render (request, 'addpost.html', context) 

# Bei allen Likefunktionen wird ein User markeirt, falls er ein Objekt liked
def LikesPostView(request, pk):
    post= Post.objects.get(id=pk)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog-details', args=[str(pk)]))
    
def DislikePostView(request, pk):
    post=Post.objects.get(id=pk)
    post.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('blog-details', args=[str(pk)]))

def LikeKommentar(request, pkPost, pkKommentar):
    kommentar=Kommentar.objects.get(id=pkKommentar)
    kommentar.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog-details', args=[str(pkPost)]))

def DislikeKommentar(request,pkPost, pkKommentar):
    kommentar=Kommentar.objects.get(id=pkKommentar)
    kommentar.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('blog-details', args=[str(pkPost)]))

def LikeUnterkommentare(request, pkPost, pkUnterkommentar):
    unterkommentar=UnterKommentar.objects.get(id=pkUnterkommentar)
    unterkommentar.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog-details',args=[str(pkPost)]))

def DislikeUnterkommentare(request,pkPost,pkUnterkommentar):
    unterkommentar=UnterKommentar.objects.get(id=pkUnterkommentar)
    unterkommentar.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('blog-details',args=[str(pkPost)]))

# Klasse für das Erstellen eines Kommentars   
class AddKommentarView(CreateView):
    model=Kommentar  
    form_class= KommentarForm
    template_name = 'addcomment.html'
    
    # Pk der Webseite Blogdetails wird angehängt und aufgerufen
    def get_success_url(self):
       return reverse_lazy('blog-details', kwargs={'pk': self.kwargs['pk']})
    #Post-Id und Username wird per Form übergeben
    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        form.instance.name = self.request.user.username
        return super().form_valid(form)

# Klasse für das Erstellen eines Unterkommentars   
class AddUnterkommentarView(CreateView):
    model= UnterKommentar
    form_class= UnterKommentarForm
    template_name='addsubcomment.html'

    # Pk der Webseite Blogdetails wird angehängt und aufgerufen
    def get_success_url(self):
       return reverse_lazy('blog-details', kwargs={'pk': self.kwargs['post']})

    # "Parent" Kommentar ID, Post-Id und Username wird per Form übergeben
    def form_valid(self,form):
        form.instance.überkommentar_id=self.kwargs['kommentar']
        form.instance.post_id=self.kwargs['post']
        form.instance.name = self.request.user.username
        return super().form_valid(form)