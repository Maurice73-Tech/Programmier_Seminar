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
from django.urls import path
from app_1.views import (registrieren, benutzer_logout, benutzer_login, profile, impressum,authentifizieren_view,add_block_view,LikesPostView,DislikePostView,ForumView, BlogDetailView,AddKommentarView,profile_edit, Passwords_View)
from app_1.models import Post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',benutzer_login,name='startseite'),
    path('impressum/',impressum,name='impressum'),
    path('forum/',ForumView.as_view (model=Post),name='forum'),
    path('blog-details/<int:pk>',BlogDetailView.as_view (model=Post),name='blog-details'),
    path('addpost/',add_block_view ,name='addpost'),
    path('admin/', admin.site.urls),
    path('login/', benutzer_login, name='login'),
    path('logout/',benutzer_logout,name='logout'),
    path('registrieren/',registrieren ,name='registrieren'),
    path('authentifizieren/',authentifizieren_view ,name='authentifizieren'),
    path('profile/',profile ,name='profile'),
    path('profile_edit/',profile_edit.as_view() ,name='profile_edit'),
    path('password/',Passwords_View.as_view(template_name='password_edit.html')),
    path('likes/<int:pk>',LikesPostView, name='like_post'),
    path('blog-details/<int:pk>/kommentieren',AddKommentarView.as_view(model=Post), name='addcomment'),
    path('dislike/<int:pk>',DislikePostView, name='dislike_post')   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)