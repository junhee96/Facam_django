from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from account.decorators import login_required
from django.db import transaction
from .forms import RegisterForm
from .models import Order
from account.models import User
from product.models import Product
from django.contrib import messages

# Create your views here.

#데코레이터 login_required먼저 함수 실행
@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'
    template_name = 'product_detail.html'

    def form_valid(self, form):
        #트랜잭션 중단안되게
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Order(
                quantity=form.data.get('quantity'),
                product=prod,
                user=User.objects.get(email=self.request.session.get('user'))
            )
            order.save()
            prod.stock -= int(form.data.get('quantity'))
            if prod.stock >= 0:
                prod.save()
        return super().form_valid(form)
    

    
    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    # kwargs 다시넘겨줌
    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(user__email=self.request.session.get('user'))
        return queryset
