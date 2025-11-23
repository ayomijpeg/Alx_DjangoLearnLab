Command to delete the book

from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
result = book.delete()

Expected Output:

>>> print(result)

(1, {'bookshelf.Book': 1})

>>> all_books = Book.objects.all()

>>> print(all_books)

<QuerySet []>
