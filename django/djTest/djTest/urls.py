"""djTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
import sys
import os
from helloapp import views

urlpatterns = [
    path('', include('helloapp.urls')),
    path('reset/', include('helloapp.urls')),
    path('on/', include('helloapp.urls')),  #开灯
    path('off/', include('helloapp.urls')),  #关灯
    path('human/', include('helloapp.urls')),  #人体红外
    path('infrared/', include('helloapp.urls')),  #遥控
]
