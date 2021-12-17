from django.test import TestCase
from app_1.models import *
from app_1.models import NeueBenutzer, Post, Kommentar, UnterKommentar



class TestModels(TestCase):
    #NeueBenutzer.objects.create_user

    def setUp(self):
        testuser = NeueBenutzer.objects.create_user('IchBinEinTestuser','testtest', 'tester',  '2020-01-01','IT', 'test@test.de','testtest123')
        testuser1 = NeueBenutzer.objects.create_user('IchBinEinTestuser1','testtest', 'tester',  '2020-01-01','IT', 'test1@test.de','testtest123')
        
   
    #Prüfen ob die erstellten Benutzer in der Datenbank angelegt wurden
    def test_user_exists(self):
        user_count = NeueBenutzer.objects.all().count()
        print(user_count)
        self.assertEqual(user_count, 2)
        self.assertNotEqual(user_count, 0)

    #Post
    def test_post(self):
        test_Post = Post('1','TestTitel', 'Ich bin ein Inhalt', '2021-12-16', 'testuser')  
        print(test_Post)

    #Kommentar
    def test_kommentar(self):
        test_kommentar = Kommentar('1','Ich bin ein Kommentar', 'Inhalt des Kommentars','2021-12-16')
        print(test_kommentar)

    #UnterKommentar     
    def test_UnterKommentar(self):
        test_UnterKommentar = UnterKommentar()
        print(test_UnterKommentar)
    
  
        

