from django.contrib import admin
from django.urls import path
from .views import SearchResultsView , books_form , books_delete , books_list

urlpatterns = [
    path('', books_form, name='books_insert'),
    path('<int:id>/', books_form, name='books_update'),
    path('delete/<int:id>/', books_delete, name='books_delete'),
    path('search/', SearchResultsView.as_view(), name='search_books'),
    path('list/', books_list, name='books_list')
]