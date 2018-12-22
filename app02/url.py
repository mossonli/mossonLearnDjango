#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from django.contrib import admin
from django.urls import path, re_path, include

from app02 import views

# 这个是全局的 应该做url的分发
urlpatterns = [


    path(r'app02_login/', views.login)
]
