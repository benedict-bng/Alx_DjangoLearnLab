from rest_framework import serializers
from .models import Author, Book
import datetime


# BookSerializer: handles serialization of Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation: publication_year cannot be in the future
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer: serializes Author and nests related books
class AuthorSerializer(serializers.ModelSerializer):
    # Nest books using BookSerializer
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    """
    Explanation:
    - `books` comes from the related_name="books" in the Book model.
    - This nests the BookSerializer inside the AuthorSerializer,
      so when you query an author, you also see their books.
    """
