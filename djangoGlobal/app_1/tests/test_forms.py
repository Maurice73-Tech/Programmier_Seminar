from django.contrib.auth.forms import UsernameField
from django.test import TestCase
from app_1.forms import Registrierungsform, Anmeldeform, AddBlogForm, KommentarForm, UnterKommentarForm, Profile_edit_form



class TestForms(TestCase):
    
    def test_Registrierungsform(self):
        form = Registrierungsform(data={
            "vorname":"Testuser1",
            "nachname":"Testnachname",
            "abteilung":"IT",
            "geburtsdatum": "2020-01-01",
            "email":"Testtest@test.com",
            "username":"Testuser1",
            "password1":"Startpasswort123",
            "password2":"Startpasswort123"
        })
        self.assertTrue(form.is_valid())
        
    #Registrierungsform mit falschen Bestätigungspasswort
    def test_Registrierungsform_wrong_password(self):
        form = Registrierungsform(data={
            "vorname":"Testuser",
            "nachname":"Testnachname",
            "abteilung":"IT",
            "geburtsdatum": "2020-01-01",
            "email":"Testtest@test.com",
            "username":"Testuser1",
            "password1":"Startpasswort123",
            "password2":"falschesPassswort"
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        print(form.errors)

    #Registrierungsform mit ungültiger Email
    def test_Registrierungsform_invalid_email(self):
        form = Registrierungsform(data={
            "vorname":"Testuser",
            "nachname":"Testnachname",
            "abteilung":"IT",
            "geburtsdatum": "2020-01-01",
            "email":"Testtesttest.com",
            "username":"Testuser1",
            "password1":"Startpasswort123",
            "password2":"Startpasswort123"
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        print(form.errors)
        
    #Registrierungsform ohne Daten
    def test_Registrierungsform_no_data(self):
        form = Registrierungsform(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)

    def test_Profile_edit_form(self):
        form = Profile_edit_form(data={
            "vorname":"Testuser1",
            "nachname":"Testnachname1",
            "abteilung":"IT",
            "geburtsdatum": "2020-01-01",
            "email":"Testtest@test.com",
            "username":"Testuser1",
            "profile_pic":""            
        })
        self.assertTrue(form.is_valid())

    def test_Anmeldeform(self):
        form = Anmeldeform(data={
            "username":"Testuser",
            "password":"Startpasswort123"
        })
        self.assertTrue(form.is_valid)

    def test_addBlogForm(self):
        form = AddBlogForm(data={
            "Titel":"Testtitel",
            "Inhalt":"Testinhalt"
        })
        self.assertTrue(form.is_valid)

    def test_Kommentarform(self):
        form = KommentarForm(data={
            "name":"Testtitel",
            "content":"Testinhalt"
        })
        self.assertTrue(form.is_valid)

    def test_Unterkommentarform(self):
        form = UnterKommentarForm(data={
            "content":"Ich bin ein Unterkommentar"
        })
        self.assertTrue(form.is_valid)
    

  