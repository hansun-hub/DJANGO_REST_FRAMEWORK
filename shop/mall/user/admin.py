from django.contrib import admin
from .models import User #user.models.User를 토대로 

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', )
    
admin.site.register(User, UserAdmin)