from django.contrib import messages
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Menu
from .views import menu_list, menu_detail, add_menu, edit_menu, delete_menu
from django.utils.text import slugify

class MenuViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.superuser = User.objects.create_superuser(username='superuser', password='superuser123', email='superuser@test.com')
        self.menu = Menu.objects.create(
            name='Test Menu',
            description='This is a test menu description.',
            people=2,
            price=19.99,
            image='test_image.jpg',
        )

    def test_menu_save_method(self):
        new_menu = Menu(name='New Menu', people=4, price=19.99) 
        new_menu.save()
        self.assertEqual(new_menu.slug, slugify(new_menu.name))

    def test_add_menu_view_post_invalid_data_superuser(self):
        self.client.login(username='superuser', password='superuser123')
        data = {} 
        response = self.client.post(reverse('menu:add_menu'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')  

    def test_add_menu_view_post_valid_data_non_superuser(self):
        self.client.login(username='testuser', password='password123')
        data = {
            'name': 'New Menu Item',
            'description': 'This is a new menu item description.',
            'people': 4,
            'price': 24.99,
        }
        response = self.client.post(reverse('menu:add_menu'), data=data)
        self.assertEqual(response.status_code, 302)

    def test_edit_menu_view_post_invalid_data_superuser(self):
        self.client.login(username='superuser', password='superuser123')
        data = {'name': ''} 
        response = self.client.post(reverse('menu:edit_menu', kwargs={'slug': self.menu.slug}), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')  

