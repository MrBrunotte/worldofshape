from django.shortcuts import render
from products.models import Product

# Create your views here.

def do_serach(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'products/programs.html', {'products': products})
