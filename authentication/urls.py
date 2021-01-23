from django.contrib import admin
from django.urls import path , include
from .views import SearchResultsView , users_form , users_delete , users_list , CustomUserView , UserOrders
from order.views import user_orders

from rest_framework import routers

router = routers.DefaultRouter()
router.register('', CustomUserView)

urlpatterns = [
    path('create/', users_form, name='users_insert'),
    path('<int:id>/profile', users_form, name='users_update'),
    path('<int:id>/delete', users_delete, name='users_delete'),
    path('search/', SearchResultsView.as_view(), name='search_users'),
    path('list/', users_list, name='users_list'),
    path('<int:id>/order/', UserOrders.as_view()),
    path('',include(router.urls))
]
