from django.urls import path
from .views import article,list,detail,zan,huifu

app_name='article'
urlpatterns=[
    path('root/',article.as_view(),name='article'),
    path('list/',list,name='list'),
    path('detail/<int:article_id>/<int:page_num>/',detail,name='detail'),
    path('zan/<int:article_id>/<int:is_zan>/',zan,name='zan'),
    path('huifu/<int:comment_id>/',huifu,name='huifu')
]