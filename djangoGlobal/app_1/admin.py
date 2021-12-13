from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from django.contrib.auth.models import Permission
from app_1.models import NeueBenutzer
from django.contrib.auth.admin import UserAdmin
from .models import Post, Kommentar


admin.site.register(Post)
admin.site.register(Kommentar)
# Admin Seite konfiguriert: Attribute angeordnet und unwichtige ausgeblendet
class UserAdminKonfig (UserAdmin):
    search_fields = ('username', 'vorname', 'nachname', 'abteilung', 'email')
    list_filter = ('username', 'vorname', 'nachname', 'abteilung', 'is_staff', 'is_active', 'email', 'taggs')
    ordering = ('username',)
    list_display =('username', 'vorname', 'nachname', 'abteilung', 'email', 'taggs')

    fieldsets =(
        (None, {'fields':('username', 'vorname', 'nachname', 'abteilung', 'email', 'geburtsdatum', 'taggs','profile_pic')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),

    )

admin.site.register (NeueBenutzer,UserAdminKonfig)