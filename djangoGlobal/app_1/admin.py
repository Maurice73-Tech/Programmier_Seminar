from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from django.contrib.auth.models import Permission
from app_1.models import NeueBenutzer
from django.contrib.auth.admin import UserAdmin
from .models import Post, Kommentar ,UnterKommentar

# Admin Seite konfiguriert: Attribute angeordnet und unwichtige ausgeblendet
class UserAdminKonfig (UserAdmin):
    search_fields = ('username', 'vorname', 'nachname', 'abteilung')
    list_filter = ('username', 'vorname', 'nachname', 'abteilung', 'is_staff', 'is_active')
    ordering = ('username',)
    list_display =('username', 'vorname', 'nachname', 'email', 'abteilung')

    fieldsets =(
        (None, {'fields':('username', 'vorname', 'nachname', 'abteilung', 'geburtsdatum','email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),

    )
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('Titel', 'Inhalt', 'Autor', 'Postdatum')

@admin.register(Kommentar)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'content', 'date_added')

@admin.register(UnterKommentar)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'content', 'parent')


admin.site.register (NeueBenutzer,UserAdminKonfig)