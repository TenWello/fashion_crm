from django.views.generic import TemplateView
from orders.models import Order
from products.models import Product
from customers.models import Customer
from django.shortcuts import render
from django.views import View


class DashboardView(TemplateView):
    template_name = 'shop/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['total_customers'] = Customer.objects.count()
        ctx['total_products']  = Product.objects.count()
        ctx['total_orders']    = Order.objects.count()
        ctx['recent_orders']   = Order.objects.order_by('-order_date')[:5]
        return ctx



class RegisterView(View):
    def get(self, request):
        return render(request, 'shop/register.html')

    def post(self, request):
        # Hozircha form ma’lumotlarini faqat konsolga chiqaramiz
        print(request.POST)
        return render(request, 'shop/register.html', {'message': 'Arizangiz qabul qilindi!'})

from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        name       = request.POST.get('name')
        birthday   = request.POST.get('birthday')
        gender     = request.POST.get('gender')
        class_     = request.POST.get('class')
        res_code   = request.POST.get('res_code')
        return redirect('shop:dashboard')
    return render(request, 'shop/register.html')
