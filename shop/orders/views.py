from django.shortcuts import render


def order_list(request):
    return render(request, 'orders/order_list.html')


def order_detail(request, id):
    return render(request, 'orders/order_detail.html', {'id': id})
