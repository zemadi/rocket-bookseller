from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'bookseller.views.home', name='home'),

    url(r'^books$', 'bookseller.views.books', name='books'),
    url(r'^books/new$', 'bookseller.views.new_book', name='new_book'),
    url(r'^books/(?P<book_id>\w+)$', 'bookseller.views.view_book', name='view_book'),
    url(r'^books/(?P<book_id>\w+)/edit$', 'bookseller.views.edit_book', name='edit_book'),
    url(r'^books/(?P<book_id>\w+)/delete$', 'bookseller.views.delete_book', name='delete_book'),

    url(r'^customers$', 'bookseller.views.customers', name='customers'),
    url(r'^customers/new$', 'bookseller.views.new_customer', name='new_customer'),
    url(r'^customers/(?P<customer_id>\w+)$', 'bookseller.views.view_customer', name='view_customer'),
    url(r'^customers/(?P<customer_id>\w+)/edit$', 'bookseller.views.edit_customer', name='edit_customer'),
    url(r'^customers/(?P<customer_id>\w+)/delete$', 'bookseller.views.delete_customer', name='delete_customer'),

    url(r'^admin/', include(admin.site.urls)),
)

