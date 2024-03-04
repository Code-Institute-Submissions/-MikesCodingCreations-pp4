from django.test import TestCase
from .models import AboutUs, History, Why_Choose_Us, Chef, Menu
from .views import home

class HomeViewTest(TestCase):

    def test_home_view_returns_200_and_context(self):
        """
        Test that the home view returns a 200 status code and the expected context.
        """
        about = AboutUs.objects.create(
            title="About Us",
            content="This is a test about us page."
        )
        history = History.objects.create(
            title="Our History",
            content="This is a test history page."
        )
        why_choose_us = Why_Choose_Us.objects.create(
            title="Why Choose Us?",
            content="This is a test reason to choose us."
        )
        chef = Chef.objects.create(
            name="John Doe",
            bio="This is a test chef bio."
        )
        menu = Menu.objects.create(
            title="Test Menu",
            description="This is a test menu description."
        )

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, about.title)
        self.assertContains(response, about.content)
        self.assertContains(response, history.title)
        self.assertContains(response, history.content)
        self.assertContains(response, why_choose_us.title)
        self.assertContains(response, why_choose_us.content)
        self.assertContains(response, menu.title)
        self.assertContains(response, menu.description)

    def test_home_view_with_empty_database(self):
        """
        Test that the home view handles an empty database gracefully.
        """
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        # Since you're not checking for specific content in an empty database,
        # you can remove the following lines or adjust them to check for 
        # expected behavior in your case.
        # self.assertNotContains(response, about.title)
        # self.assertNotContains(response, about.content)
        # ...

