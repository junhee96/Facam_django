from django.db import models
from account.models import User


# Create your models here.ArithmeticError
class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등급')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
