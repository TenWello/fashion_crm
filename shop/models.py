# shop/models.py

from django.db import models
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # Faqat mijoz ismi ko‘rinadi (murakkab so‘rovlar yo‘q)
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    stock_quantity = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name if self.customer else 'Unknown'}"

    @property
    def get_total_amount(self):
        """
        Buyurtmaning umumiy narxini hisoblaydi:
        barcha OrderItem’larning (mahsulot * miqdor) summasi
        """
        order_items = self.orderitem_set.all()
        total = sum([item.get_total_price for item in order_items])
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)

    @property
    def get_total_price(self):
        """
        Bitta qator elementining (narx * miqdor) summasi
        """
        if self.product:
            return self.product.price * self.quantity
        return 0

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
