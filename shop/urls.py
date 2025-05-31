# shop/urls.py

from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Kelajakda qo‘shimcha URL’lar qo‘shish mumkin:
    # path('customers/', views.customer_list, name='customer_list'),
    # path('products/', views.product_list, name='product_list'),
    # path('orders/', views.order_list, name='order_list'),
]
