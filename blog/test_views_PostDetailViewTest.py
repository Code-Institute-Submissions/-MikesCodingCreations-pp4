from django.test import TestCase
from .models import Post
from .views import post_detail
from django.urls import reverse

class PostDetailViewTest(TestCase):

    def test_post_detail_view_returns_200_for_valid_post(self):
        # Create a test post
        post = Post.objects.create(title="Test Post", content="This is a test post.")

        response = self.client.get(reverse('blog:post_detail', args=[post.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_context(self):
        # Create a test post
        post = Post.objects.create(title="Test Post", content="This is a test post.")

        response = self.client.get(reverse('blog:post_detail', args=[post.id]))
        self.assertEqual(response.context['post_detail'], post)
