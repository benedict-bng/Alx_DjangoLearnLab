from django.contrib import admin
from .models import Book
["admin.site.register(CustomUser, CustomUserAdmin)"]
# Custom admin class for Book model
@admin.register(Book)  # This decorator registers the model
class BookAdmin(admin.ModelAdmin):
    # WHAT ADMIN SHOWS IN LIST VIEW
    list_display = ('title', 'author', 'publication_year')
    
    # FILTERS ON THE RIGHT SIDEBAR
    list_filter = ('author', 'publication_year')
    
    # SEARCH BOX AT THE TOP
    search_fields = ('title', 'author')
    
    # PAGINATION - 25 BOOKS PER PAGE
    list_per_page = 25
    
    # EDIT FIELDS DIRECTLY IN LIST VIEW

    list_editable = ('publication_year',)
