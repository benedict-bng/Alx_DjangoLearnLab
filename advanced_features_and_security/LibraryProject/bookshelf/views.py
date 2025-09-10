from django.shortcuts import render

# Create your views here.
# advanced_features_and_security/relationship_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
from .models import Book

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

@permission_required('relationship_app.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        published_date = request.POST.get("published_date")
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('book_list')
    return render(request, 'relationship_app/book_form.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.published_date = request.POST.get("published_date")
        book.save()
        return redirect('book_list')
    return render(request, 'relationship_app/book_form.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

def book_list(request):
    # Safe ORM query, not raw SQL
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

def book_search(request):
    query = request.GET.get("q", "")
    # Avoid raw SQL injection: use ORM filtering
    results = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"books": results})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():  # Validates & sanitizes user input
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})



