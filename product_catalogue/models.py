
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
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' ' + self.description

    def detail(self):
        return self.product_detail_set.get(pk=self.id, is_active=True)

class Product_detail(models.Model):
    is_active = models.BooleanField(default=True, null=False)
    is_visibility = models.BooleanField()
    price = models.FloatField()
    price_offer = models.FloatField()
    offer_day_from = models.DateTimeField()
    offer_day_to = models.DateTimeField()
    quantity = models.FloatField()
    sku = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)