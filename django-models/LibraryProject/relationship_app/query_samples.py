from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Create an author
    author = Author.objects.create(name="Chinua Achebe", biography="Nigerian novelist")

    # Create a book for this author
    book = Book.objects.create(title="Things Fall Apart", publication_year=1958, author=author)

    # Create a library
    library = Library.objects.create(name="JKUAT Library", location="Juja, Kenya")

    # Add book to the library (ManyToMany)
    library.books.add(book)

    # Create a librarian (OneToOne with Library)
    librarian = Librarian.objects.create(name="Benedict Nderitu", library=library)

    # Query examples
    print["Author.objects.get(name=author_name)", "objects.filter(author=author)"["books.all()"]]
    print("Libraries that have 'Things Fall Apart':", book.libraries.all())
    print["Library.objects.get(name=library_name)"]



