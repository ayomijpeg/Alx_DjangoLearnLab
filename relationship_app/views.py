from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

### 1. Function-based View (FBV) ###

def book_list(request):
    """
    Function-based view to list all books.
    Renders the 'list_books.html' template.
    """
    # Query all books and prefetch the author to minimize database queries
    all_books = Book.objects.select_related('author').all()
    
    context = {
        'books': all_books
    }
    
    return render(request, 'list_books.html', context)


### 2. Class-based View (CBV) - DetailView ###

class LibraryDetailView(DetailView):
    """
    Class-based view (DetailView) to display a single Library and its books.
    """
    # 1. Specify the model this view will operate on
    model = Library
    
    # 2. Specify the template to use
    template_name = 'library_detail.html'
    
    # 3. Specify the name used for the context variable in the template
    context_object_name = 'library'
    
    # Optional: Override get_queryset to prefetch related ManyToMany data (books)
    # This optimizes the query when the template accesses library.books.all
    def get_queryset(self):
        return super().get_queryset().prefetch_related('books__author')
