from django.http import Http404
from .models import Product
from django.shortcuts import render

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/index.html', context)

def detail(request,product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404('No existe este producto')

    return render(request, 'product/detail.html', {'product': product})


