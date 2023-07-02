from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import User

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.register_url = reverse('user-registration')  # Replace 'user-registration' with your actual registration URL name

    def test_valid_user_registration(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password': 'secretpassword',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'johndoe@example.com')

    def test_missing_required_fields(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'secretpassword',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_duplicate_email_registration(self):
        # Register a user with the same email
        User.objects.create_user(
            first_name='Jane',
            last_name='Doe',
            email='johndoe@example.com',
            password='secretpassword'
        )

        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password': 'secretpassword',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

