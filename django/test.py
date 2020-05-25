import threading
import time
import socket
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