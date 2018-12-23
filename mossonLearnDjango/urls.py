"""mossonLearnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include


# 这个是全局的 应该做url的分发
urlpatterns = [
    path('admin/', admin.site.urls),


    # 路由分发
    path(r'app01/', include(('app01.url', "app01"))), # namespace 是url的名称空间
    path(r'app02/', include(('app02.url', "app02"))),
]
