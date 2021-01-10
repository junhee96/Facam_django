from django import forms
from django.contrib.auth.hashers import check_password
from .models import User

class RegisterForm(forms.Form):
    email = forms.EmailField(
    error_messages={
        'required': '이메일을 입력해주세요.'
    },
    max_length=64, label='이메일'
    )
    password = forms.CharField(
    error_messages={
        'required': '비밀번호를 입력해주세요.'
    },
    widget=forms.PasswordInput, label='비밀번호'
    )
    password_check = forms.CharField(
    error_messages={
        'required': '비밀번호를 입력해주세요.'
    },
    widget=forms.PasswordInput, label='비밀번호 확인'
    )
    
    def clean(self):
        #처음 값이 들어왓는지 확인
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        password_check = cleaned_data.get('password_check')
        
        if password != password_check:
            self.add_error('password', '비밀번호가 서로 다릅니다')
            self.add_error('password_check', '비밀번호가 서로 다릅니다')
                
        try:
            user = User.objects.get(email=email)
            self.add_error('email', '이미 가입된 이메일입니다.')
        except:
            pass
                        
            
class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        try:
            user = User.objects.get(email=email)
        except user.DoesNotExist:
            self.add_error('email', '아이디가 없습니다')
            return

        if not check_password(password, user.password):
            self.add_error('password', '비밀번호를 틀렸습니다')
                
