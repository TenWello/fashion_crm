from django.urls import path
from .views import customer_create

app_name = 'customers'
urlpatterns = [
    path('new/', customer_create, name='customer_create'),
]
