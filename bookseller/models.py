from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=40)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    favorites = models.ManyToManyField(Book)

    def __unicode__(self):
        return self.favorites
