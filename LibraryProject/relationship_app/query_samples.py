import os
import sys
import django

# 1. Add the project root directory to the Python path
# This allows Python to find 'django_models' which is the settings folder.
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

# 2. Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')

# 3. Initialize Django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def setup_initial_data():
    """Creates sample data to test the queries."""
    print("--- Setting up initial data ---")
    
    # Clean up previous data
    Librarian.objects.all().delete()
    Library.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()

    # Create Authors
    author1 = Author.objects.create(name="Jane Austen")
    author2 = Author.objects.create(name="George Orwell")
    
    # Create Books (ForeignKey)
    book1 = Book.objects.create(title="Pride and Prejudice", author=author1)
    book2 = Book.objects.create(title="Emma", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    book4 = Book.objects.create(title="Animal Farm", author=author2)

    # Create Libraries
    library_central = Library.objects.create(name="Central City Library")
    library_west = Library.objects.create(name="West End Branch")

    # Add Books to Libraries (ManyToManyField)
    library_central.books.add(book1, book2, book3, book4)
    library_west.books.add(book3, book4) # Only Orwell books here
    
    # Create Librarians (OneToOneField)
    librarian1 = Librarian.objects.create(name="Alice Smith", library=library_central)
    librarian2 = Librarian.objects.create(name="Bob Johnson", library=library_west)

    print("Data setup complete.\n")
    return author1, library_central

def run_queries(author_to_query, library_to_query):
    """Executes the required queries."""
    print("--- Executing Sample Queries ---")

    # 1. Query all books by a specific author (ForeignKey reverse lookup)
    print("\n1. Query all books by a specific author (Jane Austen):")
    # Using the related_name 'books' defined on the Book model's author field
    author_books = author_to_query.books.all() 
    for book in author_books:
        print(f"  - {book.title}")
    
    # Using the standard QuerySet filter
    author_books_qs = Book.objects.filter(author=author_to_query)
    print(f"  (Alternative QuerySet count: {author_books_qs.count()})")


    # 2. List all books in a library (ManyToManyField)
    print("\n2. List all books in a library (Central City Library):")
    # Using the ManyToMany field 'books' on the Library instance
    library_books = library_to_query.books.all()
    for book in library_books:
        # Also demonstrates accessing the Author's name via the ForeignKey
        print(f"  - {book.title} (Author: {book.author.name})")

    # Using the standard QuerySet filter reverse lookup
    library_books_qs = Book.objects.filter(libraries=library_to_query)
    print(f"  (Alternative QuerySet count: {library_books_qs.count()})")


    # 3. Retrieve the librarian for a library (OneToOneField reverse lookup)
    print("\n3. Retrieve the librarian for a library (Central City Library):")
    try:
        # Using the related_name 'librarian' defined on the Librarian model's library field
        librarian_instance = library_to_query.librarian 
        print(f"  - Librarian's Name: {librarian_instance.name}")
        
        # Accessing the Library's name from the Librarian instance
        print(f"  - Confirmed Library: {librarian_instance.library.name}")
        
    except Librarian.DoesNotExist:
        print(f"  - No librarian found for {library_to_query.name}.")

    print("\n--- Queries Complete ---")


if __name__ == '__main__':
    # Ensure to replace 'django_models' with your actual project's name if different
    try:
        author1, library_central = setup_initial_data()
        run_queries(author1, library_central)
    except Exception as e:
        print(f"An error occurred. Ensure your Django project is set up correctly and 'django_models.settings' is the correct path for your settings file.")
        print(f"Error details: {e}")
