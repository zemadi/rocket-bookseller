from django.shortcuts import render, redirect
from bookseller.forms import BookForm, ActorForm
from bookseller.models import Book, Customer


def home(request):
    return render(request, "home.html")

def books(request):
    books = Book.objects.all()
    return render(request, "books/books.html", {'books': books})

def new_book(request):
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/books")
    else:
        form = BookForm()
    data = {'form': form}
    return render(request, "books/new_book.html", data)

def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    data = {"book": book}
    return render(request, "books/view_book.html", data)

# Returns user to edit form and pulls the book object as an instance, for editing.
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method=="POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            if form.save():
                return redirect("/books/{}".format(book_id))
    else:
        form = BookForm(instance=book)

    data = {"book": book, "form": form}
    return render (request, "books/edit_book.html", data)

# Doesn't actually need a delete html page. It just makes an action on it.
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("/books")

def customers(request):
    customers = Customer.objects.all()
    return render(request, "customers/customers.html", {'customers': customers})

def new_customer(request):
    if request.method=="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/customers")
    else:
        form = CustomerForm()
    data = {'form': form }
    return render(request, "customers/new_customer.html", data)

def view_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    data = {"customer": customer}
    return render(request, "customers/view_customer.html", data)

def edit_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method=="POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            if form.save():
                return redirect("/customers/{}".format(customer_id))
    else:
        form = CustomerForm(instance=customer)

    data = {"customer": customer, "form": form}
    return render (request, "customers/edit_customer.html", data)

# Doesn't actually need a delete html page. It just makes an action on it.
def delete_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    return redirect("/customers")