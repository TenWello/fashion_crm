from django import forms
from .models import Customer, Product, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model  = Customer
        fields = ['name','email','phone']

class ProductForm(forms.ModelForm):
    class Meta:
        model  = Product
        fields = ['name','sku','price','in_stock']

class OrderForm(forms.ModelForm):
    class Meta:
        model  = Order
        fields = ['customer','product','quantity']
