from django.shortcuts import render,redirect

def login(request):
    form = loginSeite()
    return render(request,'app_1/login_beratung.html',{'form:':form})
def anmelden(request):
    form = anmeldeSeite()
    return render(request,'app_1/anmelden_beratung.html',{'form:':form})
def landing(request):
    return render(request,'app_1/landing.html') 