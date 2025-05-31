from django.urls import path
from .views import register, DashboardView

app_name = 'shop'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('register/', register, name='register'),
]
