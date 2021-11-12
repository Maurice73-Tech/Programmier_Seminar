from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models.fields import TimeField
from django.utils import timezone
from django.utils.translation import gettext_lazy
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


#class UserProfile(models.Model):
    #user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    #geburtsdatum = models.TextField()
    #abteilung = models.TextField()

    #def __str__(self):
        #return str(self.user)


class Benutzermanager(BaseUserManager):
    
    def create_superuser(self, benutzername,vorname, nachname, geburtsdatum, abteilung, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError ('Superuser muss staff= True sein')
        if other_fields.get('is_superuser') is not True:
            raise ValueError ('Superuser muss superuser= True sein')

        return self.create_user (benutzername, vorname, nachname, geburtsdatum, abteilung, password, **other_fields)
    
    def create_user(self, benutzername, vorname,nachname, geburtsdatum, abteilung, password, **other_fields):
        
        if not benutzername:
            raise ValueError(gettext_lazy('Du musst einen Benutzernamen angeben'))
        
        benutzername=self.get_by_natural_key (benutzername)
        user = self.model(benutzername=benutzername, vorname= vorname,nachname= nachname, geburtsdatum= geburtsdatum, abteilung= abteilung, **other_fields)
        user.set_password(password)
        user.save()
        return user

class NeueBenutzer(AbstractBaseUser,PermissionsMixin):
    benutzername= models.CharField (max_length=30, unique=True)
    vorname =models.CharField(max_length=30, blank=True)
    nachname =models.CharField(max_length=30, blank=True)
    geburtsdatum = models.DateField(default=datetime.now)
    abteilung = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = Benutzermanager()
    
    USERNAME_FIELD= 'benutzername'
    REQUIRED_FIELDS = ['vorname','nachname','geburtsdatum','abteilung',]

    def __str__(self):
        return str(self.benutzername)

#class Post(models.Model):
    #title = models.CharField(max_length=100)
    #content = models.TextField()
    #date_posted = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

    #def __str__(self):
        #return self.title