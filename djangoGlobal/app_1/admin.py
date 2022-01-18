#Imports
from django.contrib import admin
from app_1.models import NeueBenutzer
from django.contrib.auth.admin import UserAdmin
from .models import Post, Kommentar ,UnterKommentar

# User Model auf Admin Seite konfiguriert: Attribute angeordnet und unwichtige ausgeblendet
class UserAdminKonfig (UserAdmin):
    search_fields = ('username', 'vorname', 'nachname', 'abteilung')
    list_filter = ('username', 'vorname', 'nachname', 'abteilung', 'is_staff', 'is_active')
    ordering = ('username',)
    list_display =('username', 'vorname', 'nachname', 'email', 'abteilung')

    fieldsets =(
        (None, {'fields':('username', 'vorname', 'nachname', 'abteilung', 'geburtsdatum','email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),

    )

# Post Model auf Admin Seite konfiguriert: Attribute angeordnet und unwichtige ausgeblendet    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('Titel', 'Inhalt', 'Autor', 'Postdatum')

# Kommentar Model auf Admin Seite konfiguriert: Attribute angeordnet und unwichtige ausgeblendet    
@admin.register(Kommentar)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'kommentar', 'date_added')

# Unterkommentar Model auf Admin Seite konfiguriert: Attribute angeordnet und unwichtige ausgeblendet    
@admin.register(UnterKommentar)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'überkommentar', 'unterkommentar','date_added')

# Registrierung des User Models
admin.site.register (NeueBenutzer,UserAdminKonfig)