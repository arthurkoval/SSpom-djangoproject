from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('authentication.urls')),
    path('books/', include('book.urls')),
    path('authors/', include('author.urls')),
    path('orders/', include('order.urls'))
]
