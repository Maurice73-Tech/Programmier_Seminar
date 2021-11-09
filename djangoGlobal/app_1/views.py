from django.shortcuts import render,redirect

def login(request):
    form = loginSeite()
    return render(request,'app_1/login.html',{'form:':form})
def logout(request):
    form = logoutSeite()
    return render(request,'app_1/logout.html',{'form:':form})
def landing(request):
    return render(request,'app_1/landing.html')