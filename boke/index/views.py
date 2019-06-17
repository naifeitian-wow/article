from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from .models import UserModel
from article.models import ArticleModel,CategoryModel
from django.core.paginator import Paginator
from django.contrib import messages

class index(View):
    def get(self,request):
        articles=ArticleModel.objects.filter(recommend=1).order_by('-id')[:5]
        newarticle=ArticleModel.objects.all().order_by('-id')[:5]
        categorys=CategoryModel.objects.all()
        return render(request, 'index.html',{'articles':articles,'categorys':categorys,'newarticle':newarticle})
    def post(self,request):
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        again=request.POST.get('again','')

        user=UserModel.objects.filter(username=username)
        if user:
            return render(request,'index.html',{'error':'用户名已存在'})
        if password!=again:
            return render(request, 'index.html', {'error': '密码不相同'})
        else:
            user=UserModel()
            user.username=username
            user.password=password
            user.save()
            return redirect('/')
def city(request):
    return render(request,'head.html')
def login(request):
    categorys = CategoryModel.objects.all()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=UserModel.objects.filter(username=username,password=password)
        if user:
            request.session['user_id']=user[0].id
            request.session['username']=username
            messages.success(request,'这里是个人中心，你可以选择填你的个人信息，如果你的昵称为空的话，系统将显示你的用户名，如果头像为空的话，系统将使用默认的头像')
            return render(request,'user/userinfo.html',{'categorys':categorys})
        else:
            return render(request, 'index.html', {'error2': '用户名或密码错误','categorys':categorys})
    if request.method=='GET':
        messages.success(request, '这里是个人中心，你可以选择填你的个人信息，如果你的昵称为空的话，系统将显示你的用户名，如果头像为空的话，系统将使用默认的头像')
        return render(request, 'user/userinfo.html', {'categorys': categorys})

def exit(request):
    del request.session['user_id']
    del request.session['username']
    return redirect('/')

def list(request,type,page_num):
    categorys = CategoryModel.objects.all()
    if type==0:
        all_article=ArticleModel.objects.all()
    else:
        all_article = ArticleModel.objects.filter(category_id=type)
    paginator=Paginator(all_article,8)
    page=paginator.page(page_num)

    context={
        'categorys':categorys,
        'all_article':all_article,
        'paginator':paginator,
        'page':page,
        'type':type
    }
    return render(request,'article/list.html',context)

def mouse(request):
    return render(request,'打地鼠.html')
def piano(request):
    return render(request,'钢琴.html')