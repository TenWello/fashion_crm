# shop/urls.py
from django.urls import path
from .views import (
    DashboardView,
    CustomerListView, CustomerDetailView,
    ProductListView, ProductDetailView,
    OrderListView, OrderDetailView,
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

    # Mijozlar
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),

    # Mahsulotlar
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    # Buyurtmalar
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
