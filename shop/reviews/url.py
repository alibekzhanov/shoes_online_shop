from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),  # Страница со списком отзывов
    path('<int:id>/', views.review_detail, name='review_detail'),  # Страница с деталями отзыва
    path('create/', views.create_review, name='create_review'),  # Страница создания отзыва
]
