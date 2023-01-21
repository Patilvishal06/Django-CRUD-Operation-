from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm



def home(request):
    try:
        orders = Order.objects.all()
        customers = Customer.objects.all()
        total_customer = customers.count()
        total_orders = orders.count()

        delivered = orders.filter(status = 'out of Delivered').count()
        pending = orders.filter(status = 'Pending').count()

        context = {'orders': orders ,'customers' :customers , 'total_customer' : total_customer ,'total_orders' : total_orders,
                   'delivered' : delivered , 'pending' : pending }
        return render(request,"accounts/dashboard.html",context)
    except Exception as e:
        print(e)
2
def product(request):
    try:
        products = Product.objects.all()
        context ={ 'products': products}
        return render(request, "accounts/product.html", context)
    except Exception as e:
        print(e)

def customer(request ,pk_test):
    try:
        customer = Customer.objects.get(id = pk_test)
        orders = customer.order_set.all()
        orders_count = orders.count()
        context ={'customer' : customer ,'orders' : orders , 'orders_count' :orders_count }
        return render(request,"accounts/customer.html" ,context)
    except Exception as e:
        print(e)

def creteOrder(request):

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        print('Printing POST' ,request.POST)
    context ={'form' : form }
    return render(request ,'accounts/order_form.html' , context )

def updateOrder(request , pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance = order )
    if request.method == 'POST':
        form = OrderForm(request.POST , instance = order )
        if form.is_valid():
            form.save()
            return redirect('/')
        print('Printing POST' ,request.POST)
    context ={'form' : form }
    return render(request ,'accounts/order_form.html' , context )


def deleteOrder(request , pk):
    order = Order.objects.get(id = pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request , 'accounts/delete.html' ,context)