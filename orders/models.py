from django.db import models
from customers.models import Customer
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('processing','Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer    = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date  = models.DateTimeField(auto_now_add=True)
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order #{self.id} – {self.customer}"

    @property
    def total_amount(self):
        return sum(item.total_price for item in self.items.all())


class OrderItem(models.Model):
    order    = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price    = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.price


class Payment(models.Model):
    order         = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    amount        = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date  = models.DateTimeField(auto_now_add=True)
    method        = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Payment #{self.id} for Order #{self.order.id}"
