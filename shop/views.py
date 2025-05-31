# shop/views.py
from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Order
from django.db import models

class DashboardView(View):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        total_customers = Customer.objects.count()
        total_products = Product.objects.count()
        total_orders = Order.objects.count()
        # Buyurtmalardan daromadni hisoblaymiz
        # Faraz qilaylik, Order modelida total_amount maydoni bor
        total_revenue = Order.objects.aggregate(
            total=models.Sum('total_amount')
        )['total'] or 0

        recent_orders = Order.objects.order_by('-date_ordered')[:5]

        context = {
            "total_customers": total_customers,
            "total_products": total_products,
            "total_orders": total_orders,
            "total_revenue": total_revenue,
            "recent_orders": recent_orders,
        }
        return render(request, self.template_name, context)
