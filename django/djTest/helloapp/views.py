# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render  #跳转页面
import socket
import _thread
import threading

def default(request):
  #直接输入addr:port
  return render(request, 'home.html', {}) #第三个参数表示想要往home.html传什么参数
def reset(request):
  #重置当前网址 重置esp32端口的状态
  return render(request, 'home.html', {})
def onLight(request):
  # 开灯
  return render(request, 'home.html', {})
def offLight(request):
  # 关灯
  return render(request, 'home.html', {})
def humanInfrared(request):
  # 人体红外
  return render(request, 'home.html', {})
def infrared(request):
  # 遥控
  return render(request, 'home.html', {})
def home(request):
  return render(request, 'home.html', {})

def socket_dj():
  print(1)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(("0.0.0.0", 8080))
  s.listen(2)
  conn, addr = s.accept()
  print('Connected by', addr)
  while 1:
    data = conn.recv(1024)
    print(data)
  conn.close()
t1 = threading.Thread(target=socket_dj)
t1.start()