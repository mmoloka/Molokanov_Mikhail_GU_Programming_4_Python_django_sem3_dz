import datetime

from django.shortcuts import render, get_object_or_404
from .models import User, Order
from  datetime import date


def get_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user)
    order_products = dict()
    for order in orders:
        order_products[str(order)] = [str(product) for product in order.prducts.all()]
    context = {
        'title': 'Orders of customer',
        'user': user.name,
        'order_products': order_products,
    }
    return render(request, 'second_app/orders_of_user.html', context=context)


def get_products(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user)
    year_products = set()
    month_products = set()
    week_products = set()
    for order in orders:
        if date.today() - order.ordered_date <= datetime.timedelta(365):
            products = order.prducts.all()
            for product in products:
                year_products.add(str(product))
        if date.today() - order.ordered_date <= datetime.timedelta(30):
            products = order.prducts.all()
            for product in products:
                month_products.add(str(product))
        if date.today() - order.ordered_date <= datetime.timedelta(7):
            products = order.prducts.all()
            for product in products:
                week_products.add(str(product))
    context = {
        'title': 'Products of customer',
        'user': user.name,
        'year_products': year_products,
        'month_products': month_products,
        'week_products': week_products,
    }
    return render(request, 'second_app/products_of_user.html', context=context)
