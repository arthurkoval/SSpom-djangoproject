from django.shortcuts import render , redirect
from .models import Book
from .forms import BookForm
from django.db.models import Q
from django.views.generic import ListView


from rest_framework import viewsets
from .serializers import BookSerializer

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def books_list(request):
    context = {'books_list':Book.get_all()}
    return render(request,'books_list.html',context=context)

class SearchResultsView(ListView):
    model = Book
    template_name = 'search_books.html'
    def get_queryset(self): # new
        query = self.request.GET.get('s')
        try:
            object_list = Book.objects.filter(Q(id=query))
        except:
            object_list = Book.objects.filter(Q(name=query))
        return object_list 

def books_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = BookForm()
        else:
            book = Book.get_by_id(book_id=id)
            form = BookForm(instance = book)
        return render(request,'books_form.html',context = { 'form':form })
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.get_by_id(book_id=id)
            form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
        return books_redirect(request)


def books_delete(request,id=0):
    Book.delete_by_id(book_id=id)
    return books_redirect(request)
              
def books_redirect(request):
    return redirect('/api/v1/book/list')







