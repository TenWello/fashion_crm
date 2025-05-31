from django.contrib import admin
from django.urls import path, include

from shop.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',           include('shop.urls',      namespace='shop')),
    path('customers/', include('customers.urls', namespace='customers')),
    path('products/',  include('products.urls',  namespace='products')),
    path('orders/',    include('orders.urls',    namespace='orders')),
    path('inventory/', include('inventory.urls',namespace='inventory')),
    path('', RegisterView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
]
