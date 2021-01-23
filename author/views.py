from django.shortcuts import render , redirect
from .models import Author
from .forms import AuthorForm
from django.db.models import Q
from django.views.generic import ListView


from rest_framework import viewsets
from .serializers import AuthorSerializer

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


def authors_list(request):
    context = {'authors_list':Author.get_all()}
    return render(request,'authors_list.html',context=context)

class SearchResultsView(ListView):
    model = Author
    template_name = 'search_authors.html'
    def get_queryset(self): # new
        query = self.request.GET.get('s')
        try:
            object_list = Author.objects.filter(Q(id=query))
        except:
            object_list = Author.objects.filter(Q(name=query) | Q(surname=query))
        return object_list      

def authors_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = AuthorForm()
        else:
            user = Author.get_by_id(author_id=id)
            form = AuthorForm(instance = user)
        return render(request,'authors_form.html',context = { 'form':form })
    else:
        if id == 0:
            form = AuthorForm(request.POST)
        else:
            user = Author.get_by_id(author_id=id)
            form = AuthorForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return authors_redirect(request)

def authors_delete(request,id=0):
    Author.delete_by_id(author_id=id)
    return authors_redirect(request)


def authors_redirect(request):
    return redirect('/api/v1/author/list')