from django.shortcuts import render


def payment_list(request):
    return render(request, 'payments/payment_list.html')


def checkout(request):
    return render(request, 'payments/checkout.html')
