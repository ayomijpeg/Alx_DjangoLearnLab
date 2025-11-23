from django.db import models

# 1. Author Model (No relationship field defined here, it's the "parent" in ForeignKey)
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. Book Model (Demonstrates ForeignKey)
# A Book has ONE Author, but an Author can have MANY Books.
class Book(models.Model):
    title = models.CharField(max_length=200)
    # The 'author' field is the ForeignKey, linking each Book to a single Author.
    # on_delete=models.CASCADE means if the Author is deleted, all their books are deleted too.
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books' # allows accessing books from an Author instance: author.books.all()
    )

    def __str__(self):
        return f"{self.title} by {self.author.name}"

# 3. Library Model (Demonstrates ManyToManyField)
# A Library can have MANY Books, and a Book can be in MANY Libraries.
class Library(models.Model):
    name = models.CharField(max_length=100)
    # The 'books' field is the ManyToManyField, linking this Library to multiple Books.
    books = models.ManyToManyField(
        Book,
        related_name='libraries' # allows accessing libraries from a Book instance: book.libraries.all()
    )

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # The 'library' field is the OneToOneField, ensuring a unique link.
    # on_delete=models.CASCADE means if the Library is deleted, the Librarian record is deleted too.
    library = models.OneToOneField(
        Library, 
        on_delete=models.CASCADE, 
        related_name='librarian' # allows accessing the librarian from a Library instance: library.librarian
    )

    def __str__(self):
        return f"Librarian {self.name} at {self.library.name}"
