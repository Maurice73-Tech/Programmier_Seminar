from django.contrib.auth.forms import UsernameField
from django.test import TestCase
from app_1.forms import Registrierungsform 


class TestForms(TestCase):
    
    def test_Registrierungsform(self):
        form = Registrierungsform(data={
            "vorname":"Testuser",
            "nachname":"Testnachname",
            "abteilung":"IT",
            "geburtsdatum": "2020-01-01",
            "email":"Testtest@test.com"    
        })
        self.assertTrue(form.is_valid())
        

    def test_Registrierungsform_no_data(self):
        form = Registrierungsform(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)