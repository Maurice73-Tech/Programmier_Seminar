from django.test import TestCase
from app_1.models import *
from app_1.models import NeueBenutzer, Post, Kommentar, UnterKommentar
from django.conf import settings



class TestModels(TestCase):
    #NeueBenutzer.objects.create_user

    def setUp(self):
        testuser1 = NeueBenutzer.objects.create_user('IchBinEinTestuser1','testtest', 'tester',  '2020-01-01','IT', 'test1@test.de','testtest1234')
        testuser1.is_admin = True
        testuser1.is_staff = True
        testuser1.is_superuser = True
        testuser1.save
        
        
    #Prüfen ob der erstellte Benutzer in der Datenbank angelegt wurde
    def test_user_exists(self):
        user_count = NeueBenutzer.objects.all().count()
        print("Anzahl der User in der Datenbank: " + str(user_count))
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)
    
    #Nach Username filtern und das vergebene Passwort überprüfen
    def test_user_password(self):
        user_qs = NeueBenutzer.objects.filter(username__iexact="IchBinEinTestuser1")
        user_exists = user_qs.exists() and user_qs.count() == 1
        self.assertTrue(user_exists)
        testuser1 = user_qs.first()
        self.assertTrue(testuser1.check_password("testtest1234"))

    def test_login_url(self):
        login_url = "/login/"
        data = {"username":"IchBinEinTestuser1","password":"testtest1234"}
        response = self.client.post(login_url, data, follow=True)
        self.assertEqual(response.status_code, 200)

    #post ohne angemeldeten User
    def test_invalid_request(self):
        response = self.client.post("/addpost/", {"title":"Testtitel"})
        self.assertNotEqual(response.status_code, 200)

    #post mit angemeldeten User
    def test_valid_request(self):
        self.client.login(username="IchBinEinTestuser1", password="testtest1234")
        response = self.client.post("/addpost/", {"title":"Testtitel1"})
        self.assertEqual(response.status_code, 200)
        
    #Post
    def test_post(self):
        test_Post = Post('1','TestTitel', 'Ich bin ein Inhalt', '2021-12-16', 'testuser1')  
        print("Post: " + str(test_Post))
        
    #Kommentar
    def test_kommentar(self):
        test_kommentar = Kommentar('1','Ich bin ein Kommentar', 'Inhalt des Kommentars','2021-12-16')
        print("Kommentar: " + str(test_kommentar))
        
    #UnterKommentar     
    #def test_UnterKommentar(self):
        #test_UnterKommentar = UnterKommentar('1','1','Ich bin ein UnterKommentar', 'Inhalt des UnterKommentars')
        #print("Unterkommentar; " + str(test_UnterKommentar))
    
  
        

