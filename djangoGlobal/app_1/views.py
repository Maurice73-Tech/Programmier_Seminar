from django.shortcuts import render,redirect

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
    form = loginSeite()
    return render(request,'app_1/login_beratung.html',{'form:':form})

def registrieren(request):
    return render(request,'anmelden_beratung.html') 