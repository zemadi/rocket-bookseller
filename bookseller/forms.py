from django.forms import ModelForm
from bookseller.models import Book, Customer

__author__ = 'zhila'

class BookForm(ModelForm):
    class Meta:
        model = Book

class CustomerForm(ModelForm):
    class Meta:
        model = Customer