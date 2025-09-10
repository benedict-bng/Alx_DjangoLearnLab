from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']


<form method="POST">
    {% csrf_token %}
    <label for="title">Book Title</label>
    <input type="text" name="title" id="title">

    <label for="author">Author</label>
    <input type="text" name="author" id="author">

    <button type="submit">Submit</button>
</form>
