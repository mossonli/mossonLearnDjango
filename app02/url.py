#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from django.contrib import admin
from django.urls import path, re_path, include

from app02 import views

# 这个是全局的 应该做url的分发
urlpatterns = [


    path(r'app02_login/', views.login),
    # 名称空间
    path(r'app_namespace_url/', views.app_namespace_url, name='app_namespace_url'),

    # ajax 练习
    path(r'ajax_demo/', views.ajax_demo),
    # form表单文件上传
    path(r'file_put/', views.file_put),

    path(r'user_reg/', views.user_reg),
    # django 分页器
    path(r'page_demo/', views.page_demo)
]
