from django.shortcuts import render,redirect

def impressum(request):
    return render(request,'impressum.html')

def home(request):
    return render(request, 'login_beratung.html')

def login(request):
    form = loginSeite()
    return render(request,'app_1/login_beratung.html',{'form:':form})

def registrieren(request):
    return render(request,'anmelden_beratung.html') 