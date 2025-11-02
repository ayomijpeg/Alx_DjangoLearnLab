# (You should still have the 'book' variable, but let's retrieve it again to be safe)
>>> book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete it
>>> result = book.delete()

# See the result of the deletion
>>> print(result)
(1, {'bookshelf.Book': 1})

# Verify the database is empty
>>> all_books = Book.objects.all()
>>> print(all_books)
<QuerySet []>
