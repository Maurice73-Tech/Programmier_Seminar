from django.test import TestCase, Client
from django.urls import reverse
from app_1.models import Benutzermanager, NeueBenutzer, Post, Kommentar
from app_1.forms import Registrierungsform
from app_1.views import registrieren

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
    
    
        self.credentials = {
            'username': 'test',
            'password': 'testtest123'}
        NeueBenutzer.objects.create_user('test','testtest', 'tester',  '2020-01-01','IT', 'test@test.de','testtest123')

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        
        

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
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_add_block_view_GET(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        response = self.client.get(self.add_block_view_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'addpost.html')

    def test_authentifizieren_view_GET(self):

        response = self.client.get(self.authentifizieren_view_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentifizieren.html')

  

#get context data
#likes post view
#dislike post view
#profile edit
#like Kommentar


#POST Funktionen fehlen noch 

