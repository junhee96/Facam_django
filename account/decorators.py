from django.shortcuts import redirect
from .models import User


#함수 실행되기전 decorators로 이용하여 먼저 실행하게해줌
def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if not user:
            return redirect('login')
        return function(request, *args, **kwargs)

    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if not user:
            return redirect('login')
        
        admin = User.objects.get(email=user)
        if admin.level != 'admin':
            return redirect('home')
        
        return function(request, *args, **kwargs)

    return wrap
