from django.contrib import admin
from django.urls import path
from .views import SearchResultsView , authors_form , authors_delete , authors_list

urlpatterns = [
    path('', authors_form, name='authors_insert'),
    path('<int:id>/', authors_form, name='authors_update'),
    path('delete/<int:id>/', authors_delete, name='authors_delete'),
    path('search/', SearchResultsView.as_view(), name='search_authors'),
    path('list/', authors_list, name='authors_list'),
    
]