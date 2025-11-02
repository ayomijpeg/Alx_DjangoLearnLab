from django.contrib import admin
from .models import Book

# 1. Define a custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the display and functionality of the Book model
    in the Django admin interface.
    """
    
    # Step 2.1: Customize the list view
    # This controls which fields are shown on the main list page
    list_display = ('title', 'author', 'publication_year')
    
    # Step 2.2: Configure list filters
    # This adds a filter sidebar for the specified fields
    list_filter = ('publication_year', 'author')
    
    # Step 2.3: Configure search capabilities
    # This adds a search bar that searches the specified fields
    search_fields = ('title', 'author')

# Step 1: Register the Book model with the custom admin class
# This tells Django to use the 'BookAdmin' settings for the 'Book' model
admin.site.register(Book, BookAdmin)
