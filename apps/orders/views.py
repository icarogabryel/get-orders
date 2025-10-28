from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Order


@login_required
def orders_list(request):
    context = {
        'orders': Order.objects.all()
    }
    return render(request, 'orders/orders-list.html', context)
