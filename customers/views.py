from django.shortcuts import render, redirect
from .forms import CustomerForm

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:dashboard')
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_form.html', {'form': form})
