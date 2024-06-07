from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Страница со списком продуктов
    path('<int:id>/', views.product_detail, name='product_detail'),  # Страница с деталями продукта
]
