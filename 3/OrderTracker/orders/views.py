from django.shortcuts import render
from .models import Order

def home_view(request):
    return render(request, 'home.html')

def top_customers_view(request):
    top_customers = Order.get_top_customers()
    return render(request, 'top_customers.html', {'top_customers': top_customers})