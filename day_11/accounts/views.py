from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

# Create your views here.
from .models import *
from .forms import OrderForm


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    orders_total = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'orders_total': orders_total,
               'orders_delivered': orders_delivered,
               'orders_pending': orders_pending, }

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Products.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'accounts/create_order.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/create_order.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = order
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': form}
    return render(request, 'accounts/delete.html', context)
