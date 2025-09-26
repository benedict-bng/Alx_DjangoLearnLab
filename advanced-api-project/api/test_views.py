# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass123")

        # Create sample books
        self.book1 = Book.objects.create(title="Python Basics", author="Alice", publication_year=2020)
        self.book2 = Book.objects.create(title="Django Mastery", author="Bob", publication_year=2022)

        # Endpoints
