Get the specific book
>>> book = Book.objects.get(title="1984")

# Print its details
>>> print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
Title: 1984, Author: George Orwell, Year: 1949
