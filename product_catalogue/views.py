from django.http import Http404
from .models import Product
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index(request):
    params = request.GET.get('name')
    if params:
        products = Product.objects.filter(name__icontains=params)
    else:
        products = Product.objects.all()


    context = {'products': products}
    return render(request, 'product/index.html', context)

def detail(request,product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404('No existe este producto')

    return render(request, 'product/detail.html', {'product': product})


