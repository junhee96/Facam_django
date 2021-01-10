from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('account/register/', RegisterView.as_view(), name='register'),
    path('account/seller/', SellerView.as_view(), name='seller'),
    path('account/login/',  LoginView.as_view(), name='login'),
    path('account/logout/', logout, name='logout'),

]