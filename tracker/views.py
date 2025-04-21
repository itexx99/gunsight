from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from django.db.models import Q
from .forms import OrderForm, GunPartFormSet

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

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        formset = GunPartFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            order = form.save()
            formset.instance = order
            formset.save()
            return redirect('order_detail', order_id=order.id)
            # return redirect('order_list')  # Make sure this name matches the one in your url pattern
    else:
        form = OrderForm()
        formset = GunPartFormSet()
    return render(request, 'tracker/add_order.html', {
        'form': form,
        'formset': formset,
    })