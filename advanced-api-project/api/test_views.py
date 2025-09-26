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
 self.list_url = reverse("book-list")  # from router (ViewSet)
        self.detail_url = lambda pk: reverse("book-detail", kwargs={"pk": pk})

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_book(self):
        data = {"title": "New Book", "author": "Jane Doe", "publication_year": 2021}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django for Beginners")

    def test_update_book(self):
        data = {"title": "Updated Title", "author": "William", "publication_year": 2020}
        response = self.client.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": "Eric"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Eric")

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Clean"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Clean Code")

    def test_order_books_by_year_desc(self):
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 2020)  # newest first

    def test_unauthenticated_access_denied(self):
        self.client.logout()
        response = self.client.post(self.list_url, {"title": "Hack Attempt", "author": "Hacker", "publication_year": 2022})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
