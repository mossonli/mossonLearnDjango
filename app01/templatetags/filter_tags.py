#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'

# 自定义 过滤器
from django import template

register = template.Library()

@register.filter
def multi_filter(x, y):
    return x*y

@register.simple_tag
def multi_tag(x, y, z):
    return x*y*z