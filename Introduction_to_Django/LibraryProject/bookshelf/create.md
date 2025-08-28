# Create Operation

>>> from bookshelf.models import Book
>>> b1 = Book.objects.create(title=“1984”, author=“George Orwell”, published_year="1949")
>>> b1
<Book: Django Basics>
