from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Reservation
from .forms import ReserveTableForm
from .views import reserve_table, thank_you, reservation_management, delete_reservation


class ReservationViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='password')
        self.valid_data = {
            'full_Name': 'John Doe',
            'email': 'test@example.com',
            'phone': 1234567890,
            'guests': 2,
            'date': '2024-03-10',
            'time': '12:00:00'
        }

    def test_reserve_table_get_request(self):
        response = self.client.get(reverse('reservation:reserve_table'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ReserveTableForm)

    def test_reserve_table_post_valid_data(self):
        self.client.login(username='test_user', password='password')
        response = self.client.post(reverse('reservation:reserve_table'), self.valid_data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Reservation.objects.count(), 1)

    def test_reserve_table_post_invalid_data(self):
        self.client.login(username='test_user', password='password')
        invalid_data = {**self.valid_data, 'email': 'invalid_email'}
        response = self.client.post(reverse('reservation:reserve_table'), invalid_data)
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(Reservation.objects.count(), 0)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_thank_you_view(self):
        response = self.client.get(reverse('reservation:thank_you'))
        self.assertEqual(response.status_code, 200)

    def test_reservation_management_login_required(self):
        response = self.client.get(reverse('reservation:reservation_management'))
        self.assertEqual(response.status_code, 302) 

    def test_reservation_management_authenticated(self):
        self.client.login(username='test_user', password='password')
        response = self.client.get(reverse('reservation:reservation_management'))
        self.assertEqual(response.status_code, 200)

    def test_delete_reservation_login_required(self):
        reservation = Reservation.objects.create(
            full_Name='Test Reservation',
            email='test@example.com',
            phone=1234567890,
            guests=2,
            date='2024-03-10',
            time='12:00:00'
        )
        response = self.client.post(reverse('reservation:delete_reservation', args=[reservation.id]))
        self.assertEqual(response.status_code, 302) 

    def test_delete_reservation_authenticated(self):
        self.client.login(username='test_user', password='password')
        reservation = Reservation.objects.create(
            full_Name='Test Reservation',
            email='test@example.com',
            phone=1234567890,
            guests=2,
            date='2024-03-10',
            time='12:00:00'
        )
        response = self.client.post(reverse('reservation:delete_reservation', args=[reservation.id]))
        self.assertEqual(response.status_code, 302) 