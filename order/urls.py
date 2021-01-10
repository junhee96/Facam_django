from django.urls import path
from .views import *

urlpatterns = [
    path('', OrderList.as_view(), name='order'),
    path('create/', OrderCreate.as_view(), name='order_create'),

]