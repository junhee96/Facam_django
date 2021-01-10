from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm
from .models import User

def home(request):
    return render(request, 'home.html')

#해당 폼 보여주기
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = User(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        user.save()
        self.request.session['user'] = form.data.get('email')

        return super().form_valid(form)

    
class SellerView(FormView):
    template_name = 'seller.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = User(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='admin'
        )
        user.save()
        self.request.session['user'] = form.data.get('email')

        return super().form_valid(form)
    
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'
    
    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)

    
def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    
    return redirect('home')