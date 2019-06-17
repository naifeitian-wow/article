from django.db import models
from django.contrib import admin
import datetime
# Create your models here.
class CategoryModel(models.Model):
    category_name = models.CharField(max_length=20, null=False, verbose_name='文章分类名称')
    number = models.IntegerField(default=0, verbose_name='排序字段')

    class Meta:
        db_table = 'category'
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name
@admin.register(CategoryModel)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ('category_name','number')

class ArticleModel(models.Model):
    title=models.CharField(max_length=80,null=False,verbose_name='标题')
    jianjie=models.TextField(null=False,verbose_name='简介')
    content=models.TextField(null=False,verbose_name='内容')
    htmlcontent=models.TextField(null=False,verbose_name='带有样式')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name='文章分类')
    popular = models.IntegerField(default=0, verbose_name='人气指数')
    recommend=models.BooleanField(default=False,verbose_name='是否推荐')
    tupian=models.FileField(upload_to="static/images",verbose_name='封面图片')
    author=models.CharField(max_length=30,null=False,verbose_name='作者')
    create_time=models.CharField(max_length=100,null=False,verbose_name='创建时间')
    class Meta:
        # 自定义表名
        db_table='article'
        verbose_name='文章'
        verbose_name_plural=verbose_name
    def __str__(self):
        # 对象显示名字
        return self.title
@admin.register(ArticleModel)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ('title','content','category','popular','recommend','tupian','author','create_time')

class ZanModel(models.Model):
    person=models.CharField(max_length=50,null=False,verbose_name='点赞人')
    article=models.ForeignKey(ArticleModel,on_delete=models.CASCADE,verbose_name='点赞文章')
    is_zan=models.IntegerField(default=0)
    class Meta:
        # 自定义表名
        db_table='zan'
        verbose_name='点赞'
        verbose_name_plural=verbose_name

from index.models import UserModel
class CommentModel(models.Model):
    # 评论模型
    # 用户对评论一对多的关系
    user=models.ForeignKey(UserModel,on_delete=models.CASCADE,verbose_name='评论的用户')
    # 文章跟评论一对多的关系
    article=models.ForeignKey(ArticleModel,on_delete=models.CASCADE,verbose_name='文章')
    # 评论的内容
    content=models.CharField(max_length=140,null=False,verbose_name='评论内容')
    # 创建时间
    create_time=models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间')

    class Meta:
        db_table='comment'
        verbose_name='评论'
        verbose_name_plural=verbose_name
@admin.register(CommentModel)
class CommentAdminModel(admin.ModelAdmin):
    list_display = ('user','article','content','create_time')


class HuifuModel(models.Model):
    # 回复评论模型
    # 评论对回复一对多的关系
    comment=models.ForeignKey(CommentModel,on_delete=models.CASCADE,verbose_name='回复的评论')

    #回复人
    user=models.ForeignKey(UserModel,on_delete=models.CASCADE,verbose_name='回复人')
    content=models.CharField(max_length=140,null=False,verbose_name='回复内容')
    # 回复时间
    create_time=models.DateTimeField(default=datetime.datetime.now(),verbose_name='回复时间')

    class Meta:
        db_table='huifu'
        verbose_name='回复'
        verbose_name_plural=verbose_name
@admin.register(HuifuModel)
class HuifuAdminModel(admin.ModelAdmin):
    list_display = ('comment','user','content','create_time')