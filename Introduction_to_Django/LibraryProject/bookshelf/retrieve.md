# Retrieve Operation

>>> from bookshelf.models import Book
>>> Book.objects.all()
<QuerySet [<Book: Django Basics>]>

>>> Book.objects.get(title="Django Basics")
<Book: Django Basics>
