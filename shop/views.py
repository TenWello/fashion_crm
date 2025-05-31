# shop/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Customer, Product, Order

# Dashboard sahifasi (statistikalar, so‘nggi buyurtmalar)
class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        total_customers = Customer.objects.count()
        total_products = Product.objects.count()
        total_orders = Order.objects.count()

        recent_orders = Order.objects.order_by('-created_at')[:5]
        context = {
            'total_customers': total_customers,
            'total_products': total_products,
            'total_orders': total_orders,
            'recent_orders': recent_orders,
        }
        return render(request, self.template_name, context)

# Mijozlar ro‘yxati va tafsilotlari
class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 10  # agar sahifalash kerak bo‘lsa

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'

# Mahsulotlar ro‘yxati va tafsilotlari
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

# Buyurtmalar ro‘yxati va tafsilotlari
class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10

class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'
