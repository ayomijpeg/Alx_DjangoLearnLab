# relationship_app/urls.py

from django.urls import path
from . import views
from .models import Library

# Fetch the ID of the first library for demonstration (assuming data exists)
try:
    # Use .first() to get the primary key of an existing library record
    # This is ONLY for easy demonstration; in a real app, IDs would come from navigation
    first_library_pk = Library.objects.first().pk
except AttributeError:
    # Fallback if no data is found (shouldn't happen if query_samples ran)
    first_library_pk = 1 
except Exception:
    first_library_pk = 1

urlpatterns = [
    # 1. Function-based View (FBV) URL
    # Path: /relationship/books/
    path('books/', views.book_list, name='book_list'),
    
    # 2. Class-based View (CBV) URL
    # Path: /relationship/library/1/ (where 1 is the primary key/ID)
    path(
        'library/<int:pk>/', 
        views.LibraryDetailView.as_view(), 
        name='library_detail'
    ),
    
    # 3. Optional: A simple redirect for easy testing
    path(
        'library/',
        views.LibraryDetailView.as_view(),
        {'pk': first_library_pk}, # Pass the ID of the first library as a default
        name='default_library_detail'
    )
]
