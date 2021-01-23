from django.contrib import admin
from django.urls import path , include
from . import views
from .views import SearchResultsView , orders_delete , orders_list, orders_form, OrderView ,user_orders

from rest_framework import routers
router = routers.DefaultRouter()
router.register('', OrderView)


urlpatterns = [
    path('create', orders_form, name='orders_insert'),
    path('<int:id>/update', orders_form, name='orders_update'),
    path('delete/<int:id>/', orders_delete, name='orders_delete'),
    path('search/', SearchResultsView.as_view(), name='search_orders'),
    path('list/', orders_list, name='orders_list'),
    path('',include(router.urls))
]