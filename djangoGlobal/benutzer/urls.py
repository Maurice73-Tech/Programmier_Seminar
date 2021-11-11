from django.urls import path
from app_1 import views

urlpatterns = [
    path ('benutzer_registration/', views.registrierung_sicht, name='signup')
]