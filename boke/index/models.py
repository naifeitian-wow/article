from django.db import models
from django.contrib import admin
# Create your models here.
class UserModel(models.Model):
    username=models.CharField(max_length=20,null=False,verbose_name='用户名')
    password=models.CharField(max_length=20,null=False,verbose_name="密码")

    class Meta:
        db_table='user'
        verbose_name='用户'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.username

@admin.register(UserModel)
class UserAdminModel(admin.ModelAdmin):
    list_display = ('username', 'password')

class UserInfoModel(models.Model):
    tel=models.CharField(max_length=50,null=True,verbose_name='手机')
    sex=models.BooleanField(verbose_name='性别')
    address=models.CharField(max_length=100,null=True,verbose_name='地址')
    nick=models.CharField(max_length=30,null=True,verbose_name='昵称')
    touxiang=models.ImageField(upload_to='static/images/pic',verbose_name='头像')
    user=models.ForeignKey(UserModel,on_delete=models.CASCADE,verbose_name='用户',related_name='userinfo')

    class Meta:
        db_table='userinfo'
        verbose_name='用户详细信息'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.nick

@admin.register(UserInfoModel)
class UserInfoAdminModel(admin.ModelAdmin):
    list_display = ('tel', 'sex','address','nick','touxiang','user')