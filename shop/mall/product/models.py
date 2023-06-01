from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격') # 숫자를 적을 수 있게 
    description = models.TextField(verbose_name='상품내용')
    stock = models.IntegerField(verbose_name='재고')
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    
    def __str__(self):
        return self.name
    
    class Meta: 
        db_table = 'jung_product'
        verbose_name='상품'
        verbose_name_plural = '상품'
# Create your models here.