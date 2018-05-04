
from django.db import models


class Product(models.Model):
    list_types = (
        ('PR','Producto'),
        ('SR','Servicio'),
    )
    is_active = models.BooleanField(default=True, null=False)
    type = models.CharField(max_length=2, choices=list_types, null=False)
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=400)
    is_variation = models.BooleanField()
    code = models.CharField(max_length=50)
    is_complement = models.BooleanField()
    is_deleted = models.BooleanField()


class Product_detail(models.Model):
    is_active = models.BooleanField(default=True, null=False)
    is_visibility = models.FloatField()
    price = models.FloatField()
    price_offer = models.FloatField()
    offer_day_from = models.DateTimeField()
    offer_day_to = models.DateTimeField()
    quantity = models.FloatField()
    sku = models.FloatField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)