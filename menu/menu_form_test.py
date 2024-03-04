from django.test import TestCase
from .models import Menu
from .forms import MenuForm

class MenuFormTest(TestCase):

    def test_form_fields(self):
        """
        Test that the form includes all fields from the model except 'slug'.
        """
        form = MenuForm()
        self.assertEqual(set(form.fields.keys()), set(f.name for f in Menu._meta.fields if f.name not in ('id', 'slug')))

    def test_form_with_initial_data(self):
        """
        Test that the form can handle initial data correctly.
        """
        initial_data = {
            'title': "Test Menu",
            'description': "This is a test menu description.",
        }
        form = MenuForm(initial=initial_data)
        self.assertEqual(form.initial['title'], initial_data['title'])
        self.assertEqual(form.initial['description'], initial_data['description'])

# You can add more tests specific to your form's behavior
