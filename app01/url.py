#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from django.contrib import admin
from django.urls import path, re_path, include, register_converter

from app01 import views

# url转换器注册
# 导入转换器类
from app01.urlconverter import FourDigitYearConverter
# 注册转换器
register_converter(FourDigitYearConverter, "myconverter")


# 这个是全局的 应该做url的分发
urlpatterns = [

    re_path(r'^articles/2003/$', views.special_case_2003),
    # re_path(r'^articles/([0-9]{4})/$', views.year_archive),
    # re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    # re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
    path(r'login/', views.login),
    path(r'app01_login_reverse/', views.login_reverse, name="LOGIN"),
    # 名称空间app01
    # 在不同的app的url里面定义了相同的name，可能会导致url反解错误，使用名称空间进行解决
    path(r'app_namespace_url/', views.app_namespace_url, name='app_namespace_url'),
    # url的转换器
    path(r'app01_url_converter_month/<int:month>/', views.app01_url_converter_month),
    # 模版语法的url
    path(r'templates_lan/', views.templates_lan),
    # orm操作
    path('orm_operator/', views.orm_operator),
    path('orm_mul_table/', views.orm_mul_table),
    # orm 跨表查询
    path('orm_query/', views.orm_query),
    # from 验证
    path(r'form_demo/', views.form_demo),
    # form 的注册页面
    path(r'form_register/', views.form_register),
    # 用户认证组件
    path(r'auth_login/', views.auth_login),
    path(r'index/', views.index)
]
