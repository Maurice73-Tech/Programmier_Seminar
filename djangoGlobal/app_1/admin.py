from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from django.contrib.auth.models import Permission
from app_1.models import NeueBenutzer
from django.contrib.auth.admin import UserAdmin
from .models import Post, Kommentar ,UnterKommentar


admin.site.register(Post)
admin.site.register(Kommentar)
# Admin Seite konfiguriert: Attribute angeordnet und unwichtige ausgeblendet
class UserAdminKonfig (UserAdmin):
    search_fields = ('username', 'vorname', 'nachname', 'abteilung')
    list_filter = ('username', 'vorname', 'nachname', 'abteilung', 'is_staff', 'is_active')
    ordering = ('username',)
    list_display =('username', 'vorname', 'nachname', 'abteilung')

    fieldsets =(
        (None, {'fields':('username', 'vorname', 'nachname', 'abteilung', 'geburtsdatum',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),

    )

admin.site.register (NeueBenutzer,UserAdminKonfig)