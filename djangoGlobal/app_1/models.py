from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models.fields import TimeField
from django.utils import timezone
from django.utils.translation import gettext_lazy
from datetime import datetime



#class UserProfile(models.Model):
    #user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    #geburtsdatum = models.TextField()
    #abteilung = models.TextField()

    #def __str__(self):
        #return str(self.user)


class Benutzermanager(BaseUserManager):
    
    def create_superuser(self, username,vorname, nachname, geburtsdatum, abteilung, password, **other_fields):
       user = self.create_user (username=username, vorname= vorname,nachname= nachname, geburtsdatum= geburtsdatum, abteilung= abteilung, password=password)
       user.is_admin = True
       user.is_staff = True
       user.is_superuser = True
       user.save(using=self._db)
       return user


    #return self.create_user (username, vorname, nachname, geburtsdatum, abteilung, password, **other_fields)
    
    def create_user(self, username, vorname,nachname, geburtsdatum, abteilung, password):
        
        if not username:
            raise ValueError(gettext_lazy('Du musst einen Benutzernamen angeben'))
        
        user = self.model(username=username, vorname= vorname,nachname= nachname, geburtsdatum= geburtsdatum, abteilung= abteilung,)
        user.set_password(password)
        user.save(using=self._db)
        return user

class NeueBenutzer(AbstractBaseUser):
    username= models.CharField (max_length=30, unique=True)
    vorname =models.CharField(max_length=30, blank=True)
    nachname =models.CharField(max_length=30, blank=True)
    geburtsdatum = models.DateField(default=datetime.now)
    abteilung = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
 

    objects = Benutzermanager()
    
    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS = ['vorname' , 'nachname', 'geburtsdatum', 'abteilung']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj =None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True  

#class Post(models.Model):
    #title = models.CharField(max_length=100)
    #content = models.TextField()
    #date_posted = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

    #def __str__(self):
        #return self.title

        #asdad