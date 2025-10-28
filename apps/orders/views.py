from django.shortcuts import render

from .models import Order


def orders_list(request):
    context = {
        'orders': Order.objects.all()
    }
    return render(request, 'orders/orders-list.html', context)
