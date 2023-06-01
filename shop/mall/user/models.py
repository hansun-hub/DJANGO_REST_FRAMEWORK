from django.db import models

class User(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='생성일자')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'jung_user'
        verbose_name='사용자'
        verbose_name_plural = '사용자'
        
#회원관리에 관한 model 설정
#간단한 이메일과 비밀번호 입력하게, 
#verbose 를 설정하여 관리자 화면에서도 볼 수 있게 만들어준다.
# Create your models here.
