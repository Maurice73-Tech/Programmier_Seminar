"""djangoGlobal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_1 import views as user_views
from app_1.views import ForumView, BlogDetailView, registrieren
from app_1.views import (registrieren, benutzer_logout, benutzer_login)
from app_1.models import Post



urlpatterns = [
    path('',user_views.forum,name='forum'),
    path('impressum/',user_views.impressum,name='impressum'),
    path('forum/',ForumView.as_view (model=Post),name='forum'),
    path('blog-details/<int:pk>',BlogDetailView.as_view (model=Post),name='blog-details'),
    path('admin/', admin.site.urls),
    path('login/', benutzer_login, name='login'),
    path('logout/',benutzer_logout,name='logout'),
    path('registrieren/',registrieren ,name='registrieren'),
    path('profile/',user_views.profile,name='profile')
]
