# Update Operation

>>> from bookshelf.models import Book
>>> b1 = Book.objects.get(title="Django Basics")
>>> b1.author = "B. Nderitu"
>>> b1.save()

>>> Book.objects.get(title="Django Basics")
<Book: Django Basics>
