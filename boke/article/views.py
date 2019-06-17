from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
from .models import CategoryModel,ArticleModel,ZanModel,CommentModel,HuifuModel
from index.models import UserModel
from .utils import login_required
# 导入类视图装饰器
from django.utils.decorators import method_decorator
import datetime
from django.core.paginator import Paginator
# Create your views here.


class article(View):
    @method_decorator(login_required)
    def get(self,request):
            categorys=CategoryModel.objects.all()
            return render(request,'article/root.html',{'categorys':categorys})


def list(request):
    if request.method=='POST':
        title=request.POST.get('title','')
        content=request.POST.get('content','')
        htmlcontent=request.POST.get('htmlcontent','')
        if len(content) <= 180:
            jianjie=content
        if len(content)>180:
            jianjie=content[:180]
        category_id=request.POST.get('category_id','')
        popular=0
        recommend=request.POST.get('recommend',False)
        if recommend=='on':
            recommend=True
        tupian=request.FILES.get('tupian')
        author=request.POST.get('author','')


        article=ArticleModel()
        article.title=title
        article.content=content
        article.htmlcontent=htmlcontent
        article.jianjie=jianjie
        article.category_id=category_id
        article.popular=popular
        article.recommend=recommend
        article.tupian=tupian
        article.author=author

        date1=datetime.datetime.now()
        date2 = date1.strftime('%Yyear%mmonth%dday%Hhour%Mminute%Ssecond')
        date2 = date2.replace('year', '年').replace('month', '月').replace('day', '日').replace('hour','时').replace('minute','分').replace('second','秒')
        article.create_time =date2
        article.save()
        return redirect('/')

def detail(request,article_id,page_num):
    if request.method=='POST':
        user_id=request.session.get('user_id','')
        if user_id=='':
            pass
        else:
            content=request.POST.get('content','')
            again=CommentModel.objects.filter(user_id=user_id,article_id=article_id,content=content)
            if again:
                return redirect('/article/detail/' + str(article_id)+'/1/')
            comment=CommentModel()
            comment.user_id=user_id
            comment.article_id=article_id
            comment.content=content
            comment.create_time=datetime.datetime.now()
            comment.save()
            return redirect('/article/detail/'+str(article_id)+'/1/')

    article=ArticleModel.objects.get(id=int(article_id))
    categorys = CategoryModel.objects.all()


    user_id = request.session.get('user_id','')
    user=''
    shifou=0
    if user_id!='':
        user = UserModel.objects.filter(id=user_id)
    if user:
        zan=ZanModel.objects.filter(person=user[0],article_id=article_id)
        if zan:
            shifou=zan[0].is_zan
        else:
            shifou=0
    else:
        shifou=0

    comments=CommentModel.objects.filter(article_id=article_id).order_by('-id')
    paginator = Paginator(comments,5)
    page=paginator.page(page_num)

    context={
        'article':article,
        'categorys':categorys,
        'shifou':shifou,
        'comments':comments,
        'page': page,
        'page_num':page_num
    }
    return render(request,'article/detail.html',context)

def zan(request,article_id,is_zan):
    article = ArticleModel.objects.get(id=article_id)
    if is_zan==1:
        article.popular+=1
        article.save()
    if is_zan==0:
        article.popular -= 1
        article.save()
    user_id=request.session['user_id']
    user=UserModel.objects.filter(id=user_id)
    if user:
        user=user[0]
        z=ZanModel.objects.filter(person=user,article_id=article_id)
        if z:
            zan=z[0]
            zan.is_zan=is_zan
            zan.save()
        else:
            zan=ZanModel()
            zan.person=user
            zan.article_id=article_id
            zan.is_zan=is_zan
            zan.save()
        return JsonResponse({'success':'0'})

def huifu(request,comment_id):
    if request.method=='POST':
        user_id=request.session.get('user_id')
        content=request.POST.get('content')
        article_id=request.POST.get('article_id')
        huifu=HuifuModel()
        huifu.content=content
        huifu.user_id=user_id
        huifu.create_time=datetime.datetime.now()
        huifu.comment_id=comment_id
        huifu.save()
        return redirect('/article/detail/'+article_id+'/1/')