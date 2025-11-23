from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        # This is a helpful method that makes it easier to read
        # your Book objects in the admin panel and the shell.
        return self.title
