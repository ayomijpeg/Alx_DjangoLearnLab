Command to create a new Book instance

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

Expected Output:

>>> book

<Book: 1984>
