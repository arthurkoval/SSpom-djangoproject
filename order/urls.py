from django.contrib import admin
from django.urls import path
from . import views
from .views import SearchResultsView , orders_delete , orders_list,orders_form

urlpatterns = [
    path('', orders_form, name='orders_insert'),
    path('<int:id>/', orders_form, name='orders_update'),
    path('delete/<int:id>/', orders_delete, name='orders_delete'),
    path('search/', SearchResultsView.as_view(), name='search_orders'),
    path('list/', orders_list, name='orders_list')
]