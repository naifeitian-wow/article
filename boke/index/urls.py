from django.urls import path
from .views import index,city,login,exit,list

app_name='index'
urlpatterns=[
    path('',index.as_view(),name='index'),
    path('city/',city),
    path('login/',login,name='login'),
    path('exit/',exit,name='exit'),
    path('list/<int:type>/<int:page_num>/',list,name='list'),
]

