from django.contrib import admin
from .models import Order, OrderItem, Payment

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display   = ('id', 'customer', 'order_date', 'status', 'total_amount')
    list_filter    = ('status', 'order_date')
    search_fields  = ('customer__first_name', 'customer__last_name', 'id')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display  = ('order', 'product', 'quantity', 'price')
    list_filter   = ('product',)
    search_fields = ('product__name',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display  = ('order', 'amount', 'payment_date', 'method')
    list_filter   = ('method', 'payment_date')
    search_fields = ('order__id',)
