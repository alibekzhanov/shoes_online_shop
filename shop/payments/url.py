from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_list, name='payment_list'),  # Страница со списком платежей
    path('checkout/', views.checkout, name='checkout'),  # Страница оформления платежа
]