from django.contrib import admin
from django.urls import path, include
from . import views as tracker_views

urlpatterns = [
    path('', tracker_views.order_list, name='order_list'),  # /orders/
    path('add/', tracker_views.add_order, name='add_order'),  # /orders/add/
    path('<int:order_id>/', tracker_views.order_detail, name='order_detail'),  # /orders/1/
]
