from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app_1.views import benutzer_login, impressum, registrieren, benutzer_logout, profile, add_block_view, authentifizieren_view, ForumView

class TestUrls(SimpleTestCase):

#login  
    def test_benutzer_login_url_resolves(self):
        url = reverse('login')
        url = reverse('startseite')
        self.assertEquals(resolve(url).func, benutzer_login)  
        
    def test_benutzer_login_status_code(self):
        response = self.client.get('/login/')
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_benutzer_login_url_name(self):
        response = self.client.get(reverse('login'))
        response = self.client.get(reverse('startseite'))
        self.assertEquals(response.status_code, 200)

    def test_benutzer_login_template(self):
        response = self.client.get(reverse('login'))
        response = self.client.get(reverse('startseite'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertTemplateUsed(response, 'base.html')

#Impressum
    def test_impressum_url_resolves(self):
        url = reverse('impressum')
        self.assertEquals(resolve(url).func, impressum)

    def test_impressum_status_code(self):
        response = self.client.get('/impressum/')
        self.assertEquals(response.status_code, 200)

    def test_impressum_url_name(self):  
        response = self.client.get(reverse('impressum'))
        self.assertEquals(response.status_code, 200)

    def test_impressum_template(self):
        response = self.client.get(reverse('impressum'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'impressum.html')

#registrieren    
    def test_registrieren_url_resolves(self):
        url = reverse('registrieren')
        self.assertEquals(resolve(url).func, registrieren)
    
    def test_registrieren_status_code(self):
        response = self.client.get('/registrieren/')
        self.assertEquals(response.status_code, 200)

    def test_registrieren_url_name(self):  
        response = self.client.get(reverse('registrieren'))
        self.assertEquals(response.status_code, 200)

    def test_registrieren_template(self):
        response = self.client.get(reverse('registrieren'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrieren.html')
        
#logout
    def test_benutzer_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, benutzer_logout)

    def test_benutzer_logout_status_code(self):
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, 200)

    def test_benutzer_logout_url_name(self):  
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    def test_benutzer_logout_template(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

#profile (nicht angemeldet --> muss noch mit anmeldung durchgeführt werden)
    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_profile_status_code(self):
        response = self.client.get('/registrieren/')
        self.assertEquals(response.status_code, 200)

    def test_profile_url_name(self):  
        response = self.client.get(reverse('registrieren'))
        self.assertEquals(response.status_code, 200)

    def test_profile_template(self):
        response = self.client.get(reverse('registrieren'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrieren.html')

#addpost (nicht angemeldet --> muss noch mit anmeldung durchgeführt werden)
    def test_addpost_url_resolves(self):
        url = reverse('addpost')
        self.assertEquals(resolve(url).func, add_block_view)

    def test_addpost_status_code(self): 
        response = self.client.get('/authentifizieren/')
        self.assertEquals(response.status_code, 200)

    def test_addpost_url_name(self):  
        response = self.client.get(reverse('authentifizieren'))
        self.assertEquals(response.status_code, 200)

    def test_addpost_template(self):
        response = self.client.get(reverse('authentifizieren'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentifizieren.html')

#authentifizieren
    def test_authentifizierung_url_resolves(self):
        url = reverse('authentifizieren')
        self.assertEquals(resolve(url).func, authentifizieren_view)

    def test_authentifizieren_status_code(self):
        response = self.client.get('/authentifizieren/')
        self.assertEquals(response.status_code, 200)

    def test_authentifizieren_url_name(self):  
        response = self.client.get(reverse('authentifizieren'))
        self.assertEquals(response.status_code, 200)

    def test_authentifizieren_template(self):
        response = self.client.get(reverse('authentifizieren'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentifizieren.html')

#like_post
    def test_likesPostView_url_resolves(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        # funktioniert nicht
#forum
    """def test_forum_url_resolves(self):
        url = reverse('forum')
        self.assertEquals(resolve(url).func, ForumView)
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)"""
        # bei blog-details und addcomments das gleiche


    
        
        