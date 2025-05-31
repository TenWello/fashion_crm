from django.db import models
from products.models import Product

class Supplier(models.Model):
    name        = models.CharField(max_length=100)
    contact     = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class InventoryRecord(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory_records')
    supplier    = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    quantity    = models.IntegerField()
    date        = models.DateTimeField(auto_now_add=True)
    note        = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} – {self.quantity} pcs on {self.date.date()}"
