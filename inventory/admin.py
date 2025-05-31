from django.contrib import admin
from .models import Supplier, InventoryRecord

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display  = ('name', 'contact')
    search_fields = ('name',)

@admin.register(InventoryRecord)
class InventoryRecordAdmin(admin.ModelAdmin):
    list_display  = ('product', 'supplier', 'quantity', 'date')
    list_filter   = ('date', 'supplier')
    search_fields = ('product__name',)
