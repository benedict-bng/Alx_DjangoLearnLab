from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# ViewSet for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # All books from DB
    serializer_class = BookSerializer
