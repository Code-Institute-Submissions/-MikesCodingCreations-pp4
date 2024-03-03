from django.test import TestCase
from .models import Comment
from .forms import CommentForm

class CommentFormTest(TestCase):

    def test_form_has_fields(self):
        """
        Test that the CommentForm has the expected field.
        """
        form = CommentForm()
        self.assertEqual(list(form.fields.keys()), ['content'])

    def test_form_is_valid_with_content(self):
        """
        Test that the form is valid with valid content.
        """
        form = CommentForm(data={'content': 'This is a valid comment.'})
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_without_content(self):
        """
        Test that the form is invalid without any content.
        """
        form = CommentForm(data={'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.errors['content'])