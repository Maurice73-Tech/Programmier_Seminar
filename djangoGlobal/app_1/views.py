from django.contrib.messages.api import success
from django.db.models.fields import CommaSeparatedIntegerField
from django.http import request,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.views.generic.edit import CreateView
from app_1.forms import AddBlogForm, Registrierungsform, Anmeldeform,KommentarForm,UnterKommentarForm,Post
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView
from app_1.models import NeueBenutzer,Kommentar, Post
from django.urls import reverse_lazy,reverse

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

def benutzer_login(request):
    if request.method == 'POST':
        form = Registrierungsform(request.POST)
        username= request.POST['username']
        password= request.POST ['password']
        user = authenticate(username= username, password= password)
    
        if user:
            login (request, user)
            messages.info(request, ('Sie sind jetzt angemeldet'))
            return redirect('/forum')
        else:
            messages.info (request,'Username oder Passwort ist nicht korrekt!')

    context= {}
    return render (request, 'login.html', context)

def benutzer_logout(request):
    logout(request)
    return redirect ('/login')


def profile (request):
    user=request.user
    if not user.is_authenticated:
        return redirect ('authentifizieren')    
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

def get_context_data(self,*args,**kwargs):
    context = super(BlogDetailView,self).get_context_data(**kwargs)

    specificPost=get_object_or_404(Post,id=self.kwargs['pkPost'])
    likes=specificPost.getTotalLikes()
    context["likes"] =likes 
    return context
 

def authentifizieren_view (request):
    return render (request, 'authentifizieren.html', {})

def LikesPostView(request, pk):
    print("wird gecalled")
    print(request.POST.get('button_like'))
    print(request.POST.get('id'))
    print(request.POST.get('post_id'))
    print(request.POST.get('user_id'))
    
    #post=get_object_or_404(Post, id=request.POST.get('button_like'))
    #post.likes.add(request.NeueBenutzer)
    print("Button wird gedrückt und weitergeleitet")
    return HttpResponseRedirect(reverse('blog-details', args=[str(pk)]))

class AddKommentarView(CreateView):
    model=Kommentar  
    form_class= KommentarForm
    template_name = 'addcomment.html'
    #fields= '__all__'
    
    def get_success_url(self):
       print('posten erfolgreich')
       return reverse_lazy('blog-details', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)




