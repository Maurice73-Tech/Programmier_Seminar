from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.api import success
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import generic
from django.views.generic.edit import CreateView
from app_1.forms import AddBlogForm, Registrierungsform, KommentarForm,UnterKommentarForm, Post, Profile_edit_form, Password_change_form
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView
from app_1.models import NeueBenutzer, Kommentar, Post, UnterKommentar
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin



class ForumView (ListView):
    model = Post
    template_name = 'forum.html'
    
class BlogDetailView (DetailView):
    model = Post
    template_name = 'blog-details.html'

def benutzeruebergabe (request):
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
            messages.error(request,'Passwort oder Username ist falsch!')
    else:
        form = Registrierungsform ()
        context ['registrierungs_form'] = form

    return render(request, 'registrieren.html', context)

def benutzer_login(request):
    if request.method == 'POST':
        form = Registrierungsform(request.POST)
        username= request.POST['username']
        password= request.POST ['password']
        user = authenticate(username= username, password= password)
    
        if user:
            
            login (request, user)
            
            return redirect('/forum')
           
            
        else:        
                
                messages.error(request,'Passwort oder Username ist falsch!')

            




    context= {}
    return render (request, 'login.html', context)

def benutzer_logout(request):
    logout(request)
    messages.info(request, 'Sie wurden ausgeloggt, bis zum nächsten mal!')
    return redirect ('/login')
    

def profile (request):
    user=request.user
    if not user.is_authenticated:
        return redirect ('authentifizieren')    
    
    return render(request, 'profile.html')
    

class profile_edit (SuccessMessageMixin ,generic.UpdateView):
   form_class= Profile_edit_form 
   template_name = 'profile_edit.html'
   success_url = reverse_lazy ('profile')
   success_message = "Ihr Profil wurde geupdated!"
   

   def get_object (self):
       return self.request.user

    
       

class Passwords_View (PasswordChangeView):
    form_class = Password_change_form
    success_url = reverse_lazy ('profile')


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
        messages.info(request, "Ihre Frage wurde erstellt!")
        return redirect ('forum')
        
     
    context ['form'] = form
    

    return render (request, 'addpost.html', context) 

def get_context_data(self,*args,**kwargs):
    context = super(BlogDetailView,self).get_context_data(**kwargs)
    specificPost=get_object_or_404(Post,id=self.kwargs['post_id'])
    likes=specificPost.getTotalLikes()
    dislikes=specificPost.get
    context["likes"] ="2"
    return context
 
def authentifizieren_view (request):
    return render (request, 'authentifizieren.html', {})

def LikesPostView(request, pk):
    post= Post.objects.get(id=pk)
    post.likes.add(request.user)
    print("Button wird gedrückt und weitergeleitet")
    return HttpResponseRedirect(reverse('blog-details', args=[str(pk)]))
    
def DislikePostView(request, pk):
    post=Post.objects.get(id=pk)
    post.dislikes.add(request.user)
    print("post ist gedisliked")
    return HttpResponseRedirect(reverse('blog-details', args=[str(pk)]))

def LikeKommentar(request, pkPost, pkKommentar):
    kommentar=Kommentar.objects.get(id=pkKommentar)
    print("like Kommentar wird aufgerufen")
    kommentar.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog-details', args=[str(pkPost)]))

def LikeUnterkommentare(request, pkPost, pkUnterkommentar):
    unterkommentar=UnterKommentar.objects.get(id=pkUnterkommentar)
    unterkommentar.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog-details',args=[str(pkPost)]))

class AddKommentarView(CreateView):
    model=Kommentar  
    form_class= KommentarForm
    template_name = 'addcomment.html'
    #fields= '__all__'
    
    def get_success_url(self):
       return reverse_lazy('blog-details', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)

class AddUnterkommentarView(CreateView):
    model= UnterKommentar
    form_class= UnterKommentarForm
    template_name='addsubcomment.html'


    def get_success_url(self):
       return reverse_lazy('blog-details', kwargs={'pk': self.kwargs['post']})
    
    def form_valid(self,form):
        form.instance.parent_id=self.kwargs['kommentar']
        form.instance.post_id=self.kwargs['post']
        return super().form_valid(form)


    




