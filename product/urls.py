from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductList.as_view(), name='product'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_deatil'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('api/', ProductListAPI.as_view()),
    path('api/<int:pk>/', ProductDetailAPI.as_view()),
]