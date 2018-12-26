from django.shortcuts import render,HttpResponse
from django.urls import reverse # 用于url的反向解析

# Create your views here.

def special_case_2003(request):
    # request 是封装的请求对象
    print(request)
    print(request.GET)
    return HttpResponse("OK")

def login(request):

    return render(request, 'login.html')

def login_reverse(request):
    """
    URL反向解析
    """

    h = reverse('LOGIN') # 通过reverse配合url中的name就可以获得 当前的url

    return render(request, 'login_reverse.html')


def app_namespace_url(request):
    pat = reverse('app01:app_namespace_url')
    print(pat)
    return HttpResponse("app01 app_namespace_url")

def app01_url_converter_month(request, month):

    return HttpResponse(month)

def templates_lan(request):
    """
    模版语法
    {{}} 渲染变量，{%%}渲染标签
    """
    name = 'mosson'
    age = 18
    li = [1, 2, 3, 4]
    dic = {'name': 'mosson', 'age': 18}
    b = True
    return render(request, 'templates_lan.html', locals())
