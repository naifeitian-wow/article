from django import template
from article.models import  CommentModel,HuifuModel


# 用来注册一个自定义的标签
register=template.Library()

@register.filter
def huifu(comment_id):
    huifu_list=HuifuModel.objects.filter(comment_id=comment_id)
    return huifu_list