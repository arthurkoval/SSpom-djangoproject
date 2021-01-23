from django.contrib import admin
from django.urls import path , include
from .views import SearchResultsView , authors_form , authors_delete , authors_list , AuthorView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('', AuthorView)

urlpatterns = [
    path('create/', authors_form, name='authors_insert'),
    path('<int:id>/profile', authors_form, name='authors_update'),
    path('delete/<int:id>/', authors_delete, name='authors_delete'),
    path('search/', SearchResultsView.as_view(), name='search_authors'),
    path('list/', authors_list, name='authors_list'),
    path('',include(router.urls))
]