#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from django import forms
from django.forms import widgets
from app01.models import UserInfo

class UserForm(forms.Form):
    # label 可以用form标签展示到前端 的label标签
    name = forms.CharField(min_length=4, label="用户名",error_messages={"required":"该字段不能为空"})
    pwd = forms.CharField(min_length=4, label="密码", widget=widgets.PasswordInput)
    # r_pwd = forms.CharField(min_length=4,error_messages={"required":"不能为空"})
    email = forms.EmailField(error_messages={"required":"不能为空","invalid":"格式错误"})
    tel = forms.CharField(error_messages={"required":"不能为空"})
    sex_list = (
        (1, '男'),
        (2, '女'),
    )
    sex = forms.IntegerField(widget=(forms.Select(choices=sex_list)))




