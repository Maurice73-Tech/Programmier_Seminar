from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy
from datetime import datetime

from djangoGlobal.settings import AUTH_USER_MODEL

class Benutzermanager(BaseUserManager):
    
    def create_superuser(self, username,vorname, nachname, geburtsdatum, email, abteilung, password, **other_fields):
        user = self.create_user (username=username, vorname= vorname,nachname= nachname, geburtsdatum= geburtsdatum, email=email, abteilung= abteilung, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


    #return self.create_user (username, vorname, nachname, geburtsdatum, abteilung, password, **other_fields)
    
    def create_user(self, username, vorname,nachname, geburtsdatum, abteilung, email, taggs, password):
        
        if not username:
            raise ValueError(gettext_lazy('Du musst einen Benutzernamen angeben'))
        
        user = self.model(username=username, vorname= vorname,nachname= nachname, geburtsdatum= geburtsdatum, taggs= taggs, email=email, abteilung= abteilung,)
        user.set_password(password)
        user.save(using=self._db)
        return user

class NeueBenutzer(AbstractBaseUser, PermissionsMixin):
    username= models.CharField (max_length=30, unique=True)
    vorname =models.CharField(max_length=30, blank=True)
    nachname =models.CharField(max_length=30, blank=True)
    email =models.EmailField(max_length=30, blank=True)
    geburtsdatum = models.DateField(default=datetime.now)
    abteilung = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField (null=True, blank = True, upload_to = 'profilbilder', default='/profilbilder/default.jpg')
    taggs = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    
 

    objects = Benutzermanager()
    
    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS = ['vorname' , 'nachname', 'geburtsdatum', 'abteilung', 'email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj =None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True  

class Post(models.Model):
    title = models.CharField(max_length=100, name='Titel')
    content = models.TextField(name='Inhalt')
    date_posted = models.DateTimeField(default=timezone.now, name='Postdatum')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name= 'Autor')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='blog_posts')

    def __str__(self):
        return 'Titel: ' + self.Titel + '  / Inhalt: ' + str(self.Inhalt)

    def getTotalLikes(self):
        return self.likes.count()

class Kommentar (models.Model):
    post= models.ForeignKey(Post, related_name= "kommentare", on_delete=models.CASCADE)
    name= models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    

def addComment():
    pass

class UnterKommentar(models.Model):
    post=models.ForeignKey(Post,related_name="unterkommentar", on_delete= models.CASCADE)
    name=models.CharField(max_length=250)
    content=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return '%s - %s' % (self.post.Titel , self.name)

