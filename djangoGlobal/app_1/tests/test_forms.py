from django.test import SimpleTestCase
from app_1.forms import Registrierungsform 


class TestForms(SimpleTestCase):
    
    def test_Registrierungsform(self):
        form = Registrierungsform(data={
            'vorname':'Testuser',
            'nachname':'Testnachname',
            'abteilung':'IT',
            'geburtsdatum':'01.01.2001',
            'email':'Test@test.com'
        })

        self.assertTrue(form.is_valid())
        

    def test_Registrierungsform_no_data(self):
        form = Registrierungsform(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)