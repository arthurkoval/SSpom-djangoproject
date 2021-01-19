from django.shortcuts import render , redirect
from .models import Order
from .forms import OrderForm
from django.db.models import Q
from django.views.generic import ListView

def orders_list(request):
    context = {'orders_list':Order.get_all()}
    return render(request,'orders_list.html',context=context)

class SearchResultsView(ListView):
    model = Order
    template_name = 'search_orders.html'
    def get_queryset(self): # new
        query = self.request.GET.get('s')
        try:
            object_list = Order.objects.filter(Q(id=query))
            return object_list
        except:
            return []
     
def orders_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = OrderForm()
        else:
            order = Order.get_by_id(order_id=id)
            form = OrderForm(instance = order)
        return render(request,'orders_form.html',context = { 'form':form })
    else:
        if id == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.get_by_id(order_id=id)
            form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
        return orders_redirect(request)

def orders_delete(request,id=0):
    Order.delete_by_id(order_id=id)
    return orders_redirect(request)


def orders_redirect(request):
    return redirect('/orders/list')

