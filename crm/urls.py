# crm/urls.py
from django.contrib import admin
from django.urls import path
from shop.views import DashboardView  # bu joy to‘g‘ri import qilinishi kerak

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),
    # boshqa sahifalar, masalan:
    # path('customers/', CustomerListView.as_view(), name='customer_list'),
    # path('orders/', OrderListView.as_view(), name='order_list'),
    # path('products/', ProductListView.as_view(), name='product_list'),
]
