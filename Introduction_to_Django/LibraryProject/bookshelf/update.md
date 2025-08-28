# Update Operation

>>> from bookshelf.models import Book
>>> b1 = Book.objects.get(title=“Nineteen Eighty-Four”)
>>> b1.author = “George Orwell”
>>> b1.save()

>>> Book.objects.get(title=“Nineteen Eighty-Four”)
<Book: Django Basics>
