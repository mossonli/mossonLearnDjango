#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from django import forms
from django.forms import widgets
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

from app01.models import UserInfo
"""
渲染 input 标签widget=TextInput()
错误信息 error_message={"required":"该字段不能为空"}
通过form标签 设置标签的属性：

"""


class UserForm(forms.Form):
    name = forms.CharField(min_length=4, label="用户名", error_messages={"required":"该字段不能为空"},
                           widget=widgets.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(min_length=6, widget=widgets.PasswordInput())
    repwd = forms.CharField()
    email = forms.CharField(error_messages={"required":"该字段不能为空", "invalid":"格式错误"})
    tel = forms.CharField()

    def clean_name(self):
        val = self.cleaned_data.get('name')
        ret = UserInfo.objects.filter(name=val)
        if not ret:
            return val
        else:
            raise ValidationError("该用户已经注册")


    def clean(self):
        """ clean 方法是Form父类中的方法
            重写父类的clean作为全局钩子函数
        """
        pwd = self.cleaned_data.get('pwd')
        repwd = self.cleaned_data.get('repwd')
        if pwd and repwd: # 先校验 pwd 和 repwd是不是符合校验规则
            if pwd == repwd:
                return self.cleaned_data
            else:
                return ValidationError("两次密码不一致")
        else:
            return self.cleaned_data