from django.test import TestCase, Client
from .models import Post, Category
from .views import post_list
from django.urls import reverse

class PostListViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_post_list_view_returns_200(self):
        # Create a few test posts
        Post.objects.create(title="Test Post 1", content="This is a test post.")
        Post.objects.create(title="Test Post 2", content="Another test post.")

        url_name = 'blog:post_list'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_context(self):
        # Create a test post
        post = Post.objects.create(title="Test Post", content="This is a test post.")

        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(list(response.context['post_list']), [post])