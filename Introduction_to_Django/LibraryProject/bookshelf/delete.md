# Delete Operation

>>> from bookshelf.models import Book
>>> b1 = Book.objects.get(title="Django Basics")
>>> b1.delete()
(1, {'bookshelf.Book': 1})
["book.delete"]
>>> Book.objects.all()
<QuerySet []>
