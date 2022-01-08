from django.test import TestCase
from django.urls import reverse, resolve
from app_1.views import benutzer_login, impressum, registrieren, benutzer_logout, profile, add_block_view, authentifizieren_view, ForumView, LikesPostView
from app_1.models import NeueBenutzer


class TestUrls(TestCase):
     
    def setUp(self):
        self.credentials = {
            'username': 'test',
            'password': 'testtest123'}
        NeueBenutzer.objects.create_user('test','testtest', 'tester',  '2020-01-01','IT', 'test@test.de','testtest123')
    def test_login(self):
        # login daten senden
        response = self.client.post('/login/', self.credentials, follow=True)
        # sollte eingeloggt sein
        self.assertTrue(response.context['user'].is_authenticated)

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

#profile (nicht angemeldet)
    def test_profile_url_resolves1(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_profile_status_code1(self):
        response = self.client.get('/authentifizieren/')
        self.assertEquals(response.status_code, 200)

    def test_profile_url_name1(self):  
        response = self.client.get(reverse('authentifizieren'))
        self.assertEquals(response.status_code, 200)

    def test_profile_template1(self):
        response = self.client.get(reverse('authentifizieren'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentifizieren.html')

#profile (angemeldet)
    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_profile_status_code(self):
        # login daten senden
        response = self.client.post('/login/', self.credentials, follow=True)
        # sollte eingeloggt sein
        self.assertTrue(response.context['user'].is_authenticated)
        response = self.client.get('/profile/')
        self.assertEquals(response.status_code, 200)

    def test_profile_url_name(self):  
        # login daten senden
        response = self.client.post('/login/', self.credentials, follow=True)
        # sollte eingeloggt sein
        self.assertTrue(response.context['user'].is_authenticated)
        response = self.client.get(reverse('profile'))
        self.assertEquals(response.status_code, 200)

    def test_profile_template(self):
        # login daten senden
        response = self.client.post('/login/', self.credentials, follow=True)
        # sollte eingeloggt sein
        self.assertTrue(response.context['user'].is_authenticated)
        response = self.client.get(reverse('profile'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

#addpost (nicht angemeldet)
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

#addpost (angemeldet)
    def test_addpost_url_resolves(self):
        url = reverse('addpost')
        self.assertEquals(resolve(url).func, add_block_view)

    def test_addpost_status_code(self): 
        # login daten senden
        response = self.client.post('/login/', self.credentials, follow=True)
        # sollte eingeloggt sein
        self.assertTrue(response.context['user'].is_authenticated)
        response = self.client.get('/forum/')
        self.assertEquals(response.status_code, 200)

    def test_addpost_url_name(self):  
        # login daten senden
        response = self.client.post('/login/', self.credentials, follow=True)
        # sollte eingeloggt sein
        self.assertTrue(response.context['user'].is_authenticated)
        response = self.client.get(reverse('forum'))
        self.assertEquals(response.status_code, 200)

    def test_addpost_template(self):
        # login daten senden
        response = self.client.post('/login/', self.credentials, follow=True)
        # sollte eingeloggt sein
        self.assertTrue(response.context['user'].is_authenticated)
        response = self.client.get(reverse('forum'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum.html')

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

#blog-details   
    def test_blog_post_details_resolves(self):
        url = reverse('blog-details', args=[1])
        self.assertEqual(url, '/blog-details/1')
        resolver = resolve('/blog-details/1')
        self.assertEqual(resolver.view_name, 'blog-details')
        
#like_post
    def test_like_post_url_resolves(self):
        url = reverse('like_post', args=[1])
        self.assertEqual(url, '/likes/1')
        resolver = resolve('/likes/1')
        self.assertEqual(resolver.view_name, 'like_post')

#dislike_post
    def test_dislike_post_url_resolves(self):
        url = reverse('dislike_post', args=[1])
        self.assertEqual(url, '/dislike/1')
        resolver = resolve('/dislike/1')
        self.assertEqual(resolver.view_name, 'dislike_post')

#Kommentar_likes
    def test_kommentar_likes_url_resolves(self):
        url = reverse('kommentar_likes', args=[1,1])
        self.assertEqual(url, '/Klikes/1/1')
        resolver = resolve('/Klikes/1/1')
        self.assertEqual(resolver.view_name, 'kommentar_likes')


    
        
        