from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app_1.views import forum, benutzer_login, impressum, registrieren, benutzer_logout, profile, add_block_view, authentifizieren_view

class TestUrls(SimpleTestCase):

    def test_forum_url_resolves(self):
        url = reverse('forum')
        print(resolve(url))
        
    def test_benutzer_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, benutzer_login)

    def test_impressum_url_resolves(self):
        url = reverse('impressum')
        self.assertEquals(resolve(url).func, impressum)

    def test_registrieren_url_resolves(self):
        url = reverse('registrieren')
        self.assertEquals(resolve(url).func, registrieren)

    def test_benutzer_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, benutzer_logout)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_addpost_url_resolves(self):
        url = reverse('addpost')
        self.assertEquals(resolve(url).func, add_block_view)

    def test_authentifizierung_url_resolves(self):
        url = reverse('authentifizieren')
        self.assertEquals(resolve(url).func, authentifizieren_view)



    
        
        