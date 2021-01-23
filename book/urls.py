from django.contrib import admin
from django.urls import path , include
from .views import SearchResultsView , books_form , books_delete , books_list , BookView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('', BookView)

urlpatterns = [
    path('create/', books_form, name='books_insert'),
    path('<int:id>/profile', books_form, name='books_update'),
    path('delete/<int:id>/', books_delete, name='books_delete'),
    path('search/', SearchResultsView.as_view(), name='search_books'),
    path('list/', books_list, name='books_list'),
    path('',include(router.urls))
]