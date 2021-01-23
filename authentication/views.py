from django.shortcuts import render , redirect
from .models import CustomUser
from .forms import UserForm
from django.db.models import Q
from django.views.generic import ListView
from order.models import Order

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .serializers import CustomUserSerializer , UserOrdersSerializer

class CustomUserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
   
class UserOrders(ListAPIView):
    serializer_class = UserOrdersSerializer
    def get(self, request, *args, **kwargs):
        self.queryset = Order.objects.filter(user=kwargs['id'])
        return self.list(request, *args, **kwargs)

def users_list(request):
    context = {'users_list':CustomUser.get_all()}
    return render(request,'users_list.html',context=context)

class SearchResultsView(ListView):
    model = CustomUser
    template_name = 'search_users.html'
    def get_queryset(self): # new
        query = self.request.GET.get('s')
        try:
            object_list = CustomUser.objects.filter(Q(id=query))
        except:
            object_list = CustomUser.objects.filter(Q(first_name=query) | Q(last_name=query) | Q(email=query))
        return object_list      

def users_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = UserForm()
        else:
            user = CustomUser.get_by_id(user_id=id)
            form = UserForm(instance = user)
        return render(request,'users_form.html',context = { 'form':form })
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = CustomUser.get_by_id(user_id=id)
            form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return users_redirect(request)
        
def users_delete(request,id=0):
    CustomUser.delete_by_id(user_id=id)
    return users_redirect(request)

def users_redirect(request):
    return redirect('/api/v1/user/list')

    
