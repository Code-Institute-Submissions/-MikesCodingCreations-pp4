from django.test import TestCase
from .models import Reservation
from .forms import ReserveTableForm


class ReserveTableFormTests(TestCase):

    def test_form_has_expected_fields(self):
        form = ReserveTableForm()
        expected_fields = {
            'full_Name', 'email', 'phone', 'guests', 'date', 'time'
        } 
        self.assertEqual(set(form.fields.keys()), expected_fields)

    def test_full_name_field_is_required(self):
        form = ReserveTableForm({'full_Name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_Name'], ['This field is required.'])

    def test_phone_field_is_required(self):
        form = ReserveTableForm({'phone': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['phone'], ['This field is required.'])

    def test_email_field_is_required(self):
        form = ReserveTableForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])

    def test_email_field_is_valid(self):
        data = {
            'full_Name': 'John Doe',
            'email': 'test@example.com',
            'phone': 1234567890, 
            'guests': 2,
            'date': '2024-03-10', 
            'time': '12:00:00'  
        }
        form = ReserveTableForm(data)
        print(form.errors)  

        self.assertTrue(form.is_valid(), msg="Form should be valid with all required data")

    def test_phone_field_has_integer_validation(self):
        form = ReserveTableForm({'phone': 'not-a-number'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['phone'], ['Enter a whole number.'])
