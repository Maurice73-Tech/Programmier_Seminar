from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import RequestContext


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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('Post Request wurder erkannt')
        print(form.fields)
        if form.is_valid():
            print('form is valid.')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            passwordValidation = form.cleaned_data.get('password2')
            messages.success(request, f'Account registriert für {username},{password},{passwordValidation}!')
            return redirect('login')
        else:print('form is invalid!',form.errors)
    else:
        
        form = UserCreationForm()
    return render(request, 'anmelden_beratung.html', {'form': form})

def forum(request):
    return render(request,'forum.html')