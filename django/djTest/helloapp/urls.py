from django.contrib import admin
from django.urls import path
from . import views  #.当前目录
from django.views.static import serve

urlpatterns = [
  path('', views.default, name="default"),  #addr:port
  path('reset/', views.reset, name="reset"),  #复位
  path('onLight/', views.onLight, name="webOnLight"),  #开灯
  path('offLight/', views.offLight, name="webOffLight"),  #关灯
  path('human/', views.humanInfrared, name="ultrasound"),  #人体红外
  path('infrared/', views.infrared, name="infrared"),  #遥控红外控制灯
  # path('aa/', views.hehe, name="hehe"),  
]