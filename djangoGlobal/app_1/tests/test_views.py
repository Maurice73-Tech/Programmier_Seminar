from django.test import TestCase, Client
from django.urls import reverse
from app_1.models import Benutzermanager, NeueBenutzer, Post, Kommentar

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.forum_url = reverse('forum')
        self.impressum_url = reverse('impressum')
        self.registrieren_url = reverse('registrieren')
        self.forum_url = reverse('forum')
        self.benutzer_login_url = reverse('login')
        self.benutzer_logout_url = reverse('login')
        self.profile_url = reverse('profile')
        self.add_block_view_url = reverse('addpost')
        self.authentifizieren_view_url = reverse('authentifizieren')
        

    def test_benutzerübergabe_GET(self):
        
        response = self.client.get(self.forum_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum.html')

    def test_impressum_GET(self):
        
        response = self.client.get(self.impressum_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'impressum.html')

    def test_registrieren_GET(self):
        
        response = self.client.get(self.registrieren_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrieren.html')

    def test_forum_GET(self):
        
        response = self.client.get(self.forum_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum.html')

    def test_benutzer_login_GET(self):

        response = self.client.get(self.benutzer_login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_benutzer_logout_GET(self):

        response = self.client.get(self.benutzer_logout_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_profile_GET(self):
#Hier wird ein User benötigt
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_add_block_view_GET(self):
#Hier wird ein User benötigt
        response = self.client.get(self.add_block_view_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'addpost.html')

    def test_authentifizieren_view_GET(self):

        response = self.client.get(self.authentifizieren_view_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentifizieren.html')

#POST Funktionen fehlen noch 

