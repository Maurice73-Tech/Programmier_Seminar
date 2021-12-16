from django.test import TestCase
from app_1.models import *
from app_1.models import NeueBenutzer



class TestModels(TestCase):
    #user anlegen

    def setUp(self):
        #testuser = User(self, username= 'TestUser', vorname= 'testtest', nachname='tester', geburtsdatum= '2020-01-01', abteilung='IT', email='test@test.de',taggs= '1',password= 'testtest123')
        testuser = NeueBenutzer.objects.create_user('test','testtest', 'tester',  '2020-01-01','IT', 'test@test.de', '*','testtest123')
        print(testuser.email)
        testuser1 = NeueBenutzer.objects.create_user('tester','testtest', 'tester',  '2020-01-01','IT', 'test1@test.de', '*','testtest123')
        print(testuser1.email)
    #def test_create_superuser(self):
        #testuser1 = NeueBenutzer.objects.create_superuser('test1','testtest1', 'tester',  '2020-01-01','test111@test.de','IT','testtest1234',)
       # print(testuser1.email)
#username,vorname, nachname, geburtsdatum, email, abteilung, password, **other_fields):

    def test_user_exists(self):
        user_count = NeueBenutzer.objects.all().count()
        print(user_count)
        self.assertEqual(user_count, 2)
        self.assertNotEqual(user_count, 0)

