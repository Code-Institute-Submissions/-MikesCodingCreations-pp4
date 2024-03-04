from django.test import TestCase, Client
from .models import Post, Category
from .views import post_by_category
from django.urls import reverse

class PostByCategoryViewTest(TestCase):

    def setUp(self):
        self.client = Client()

        # Create a test category
        self.category = Category.objects.create(category_name="Test Category")

        # Create posts with the category
        Post.objects.create(title="Test Post in Category", content="This is a test post.", category=self.category)
        Post.objects.create(title="Another Post", content="This is another post.", category=Category.objects.create(category_name="Another Category"))

    def test_post_by_category_view_returns_200(self):
        response = self.client.get(reverse('blog:post_by_category', args=[self.category.category_name]))
        self.assertEqual(response.status_code, 200)

    def test_post_by_category_view_context(self):
        response = self.client.get(reverse('blog:post_by_category', args=[self.category.category_name]))
        self.assertEqual(list(response.context['post_list']), [Post.objects.get(title="Test Post in Category")])