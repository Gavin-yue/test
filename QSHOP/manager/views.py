from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from  QSHOP.common import set_password
from .models import Manager,Type
import json
from django.http import JsonResponse
from goods.models import Goods


# Create your views here.
def base(request):
    return render(request,'manage_base.html')

def index(request):
    manager_name = request.session.get("manager_name")
    # id = request.session["id"]
    manager=request.COOKIES.get("manager")
    print(manager_name,manager,id)
    if manager_name and manager:
        return render(request,'common/index.html')
    else:
        return HttpResponseRedirect('/manager/login')


def register(request):
    error = ""
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        repeat_password = data.get('repeat_password')
        print(name,email,password,repeat_password)
        if password != repeat_password:
            error = "两次密码不一致"
            return render(request, 'common/register.html', {'error': error})
        md5_pwd = set_password(set_password(password))
        m=Manager.objects.filter(manager_name=name)
        if not m.exists():
            m=Manager.objects.create(manager_name=name,email=email,password=md5_pwd)
            print(m,type(m))
            return HttpResponseRedirect('/manager/login')
        error = "用户名重复"
    return render(request,'common/register.html',{'error':error})

def check_username(request):
    result = {"flag":0}
    data = request.GET
    username = data.get("username")
    print(username)
    if username != "":
        m = Manager.objects.filter(manager_name=username)
        if not m.exists():
            result["flag"] = 1
        # message= "用户名重复"
    return HttpResponse(json.dumps(result))

def login(request):
    error=""
    if request.method=="POST":
        data = request.POST
        manager_name = data.get("username")
        password = data.get("password")
        # print(manager_name,password)
        md5_pwd = set_password(set_password(password))
        # print(md5_pwd)
        try:
            m = Manager.objects.get(manager_name=manager_name,password=md5_pwd)
            #设置session
            request.session['manager_name'] = manager_name
            request.session['id'] = m.id
            #设置cookie
            response = HttpResponseRedirect('/manager/index')
            response.set_cookie("manager",manager_name)
            return response
        except:
            error = "用户名密码有误"

    return render(request,'common/login.html',{'error':error})

def logout(request):
    request.session.clear()
    response = HttpResponseRedirect('/manager/login')
    response.delete_cookie('manager')
    return response


def add_goods(request):

    manager_name = request.session.get("manager_name")
    # id = request.session["id"]
    manager = request.COOKIES.get("manager")
    if manager_name and manager:
        if request.method == "POST":
            data = request.POST
            goods_name = data.get("goods_name")
            goods_opice = data.get("goods_opice")
            goods_xprice = data.get("goods_xprice")
            goods_count = data.get("goods_count")
            goods_production = data.get("goods_production")
            safe_date = data.get("safe_date")
            goods_method = data.get("goods_method")
            goods_description = data.get("goods_description")
            goods_pic = request.FILES.get('goods_pic')
            goods_addresss = data.get("goods_addresss")
            goods_info = data.get("goods_info")
            manager_id = request.session.get("id")
            type = data.get("type")
            status = data.get("status")

            Goods.objects.create(
                goods_name=goods_name,
                goods_opice=goods_opice,
                goods_xprice=goods_xprice,
                goods_count=goods_count,
                goods_production=goods_production,
                safe_date=safe_date,
                goods_method=goods_method,
                goods_description=goods_description,
                goods_pic=goods_pic,
                goods_addresss=goods_addresss,
                goods_info=goods_info,
                manager_id=manager_id,
                type_id=type,
                # type=Type.objects.get(id=type),
                status=status,
            )
            return HttpResponse("商品添加成功")
    else:
        return HttpResponseRedirect('/manager/login')

    type_list = Type.objects.all()
    return render(request,'common/add_goods.html',{"type_list":type_list})
