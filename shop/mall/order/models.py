from django.db import models

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='사용자') #user app내의 models. User라는 클래스를 외래키로 사용하겠다. 
                                                                                        #on_delete = models.CASCADE user라는 데이터값이 삭제될때 같이 삭제시키겠음
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='주문시간')
    
    
    class Meta:
        db_table = 'jung_order'     #데이터베이스 테이블명 지정
        verbose_name='주문'         #django-admin 에서 보는 이름 지정
        verbose_name_plural = '주문' # django-admin에서 보는 복수형 이름도 지정
        
""" 
외래키를 사용하여 user app폴더 내의 models.py 내의 user클래스에서 외래키를 가져오겠다. 
on_delete=models.CASCADE 는 만일 user, product 데이터 값이 삭제될때 지금 Order의 설정한 models Order 클래스내의 있는 데이터값도 같이 지우겠다는 설정
"""
        
