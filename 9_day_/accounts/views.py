from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *


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


def customer(request):
    return render(request, 'accounts/customer.html')
