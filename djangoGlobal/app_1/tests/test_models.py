from django.test import TestCase
from app_1.models import *
from app_1.models import NeueBenutzer



class TestModels(TestCase):
    #NeueBenutzer.objects.create_user

    def setUp(self):
        testuser = NeueBenutzer.objects.create_user('IchBinEinTestuser','testtest', 'tester',  '2020-01-01','IT', 'test@test.de','testtest123')
        print(testuser)
        testuser1 = NeueBenutzer.objects.create_user('IchBinEinTestuser1','testtest', 'tester',  '2020-01-01','IT', 'test1@test.de','testtest123')
        print(testuser1)
   
    #Prüfen ob die erstellten Benutzer in der Datenbank angelegt wurden
    def test_user_exists(self):
        user_count = NeueBenutzer.objects.all().count()
        print(user_count)
        self.assertEqual(user_count, 2)
        self.assertNotEqual(user_count, 0)
        
      
        

