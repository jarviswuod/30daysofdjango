from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'accounts/dashboard.html')
    # return HttpResponse('Home rendered')

def products(request):
    return render(request,'accounts/products.html')
#     return HttpResponse('Accounts rendered')


def customer(request):
    return render(request,'accounts/customer.html')
#     return HttpResponse('customers rendered')