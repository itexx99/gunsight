from django.shortcuts import render, get_object_or_404
from .models import Order
from django.db.models import Q

def home(request):
    return render(request, 'tracker/home.html')

def order_list(request):
    query = request.GET.get('q')
    orders = Order.objects.all().order_by('-date_in')

    if query:
        orders = orders.filter(
            Q(id__icontains=query)  # Search by order ID (number)
        )

    return render(request, 'tracker/order_list.html', {'orders': orders, 'query': query})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'tracker/order_detail.html', {'order': order})
