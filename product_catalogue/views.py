from django.http import Http404
from .models import Product
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def index(request):
    params = request.GET.get('name')
    if params:
        products_list = Product.objects.filter(Q(name__icontains=params) | Q(description__icontains=params)).distinct()
    else:
        products_list = Product.objects.all()

    paginator = Paginator(products_list, 25)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'products': products}
    return render(request, 'product/index.html', context)

def detail(request,product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404('No existe este producto')

    return render(request, 'product/detail.html', {'product': product})


