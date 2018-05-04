
from django.contrib import admin

from .models import Product
from .models import Product_detail

admin.site.register(Product)

admin.site.register(Product_detail)