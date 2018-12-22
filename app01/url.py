#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from django.contrib import admin
from django.urls import path, re_path, include

from app01 import views

# 这个是全局的 应该做url的分发
urlpatterns = [

    re_path(r'^articles/2003/$', views.special_case_2003),
    # re_path(r'^articles/([0-9]{4})/$', views.year_archive),
    # re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    # re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
    path(r'login/', views.login)
]
