from django.contrib import admin
from django.urls import path
from .views import SearchResultsView , users_form , users_delete , users_list

urlpatterns = [
    path('', users_form, name='users_insert'),
    path('<int:id>/', users_form, name='users_update'),
    path('delete/<int:id>/', users_delete, name='users_delete'),
    path('search/', SearchResultsView.as_view(), name='search_users'),
    path('list/', users_list, name='users_list')
]

