from django.test import TestCase
from .models import AboutUs, History, Why_Choose_Us, Chef
from .views import aboutus_list

class AboutUsListViewTest(TestCase):

    def test_aboutus_list_view_returns_200_and_context(self):
        """
        Test that the aboutus_list view returns a 200 status code and the expected context.
        """
        about = AboutUs.objects.create(
            title="AboutUs",
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

        response = self.client.get('/aboutus/')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, about.title)
        self.assertContains(response, about.content) 
        self.assertContains(response, history.title)
        self.assertContains(response, history.content) 
        self.assertContains(response, why_choose_us.title)
        self.assertContains(response, why_choose_us.content) 
        self.assertContains(response, chef.name)
        self.assertContains(response, chef.bio) 

    def test_aboutus_list_view_with_empty_database(self):
        """
        Test that the aboutus_list view handles an empty database gracefully.
        """

        response = self.client.get('/aboutus/')

        self.assertEqual(response.status_code, 404)  