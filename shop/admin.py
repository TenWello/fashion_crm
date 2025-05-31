# shop/admin.py
from django.contrib import admin
from .models import Customer, Product, Order, OrderItem

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    search_fields = ('name',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total_amount', 'created_at')
    list_filter = ('status',)
    inlines = [OrderItemInline]
    search_fields = ('customer__first_name', 'customer__last_name')
