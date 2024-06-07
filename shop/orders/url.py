from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),  # Страница со списком заказов
    path('<int:id>/', views.order_detail, name='order_detail'),  # Страница с деталями заказа
]