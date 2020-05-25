#from moudle import *
#print(areyouok('are you ok?'))
#print(gg)
import _thread
import time

def printTime(threadName, delay):
  count = 0
  while count < 5:
    time.sleep(delay)
    count += 1
    print("%s: %s" % (threadName, time.ctime(time.time())))

try:
  _thread.start_new_thread(printTime, ("Thread-1", 2, ))
  _thread.start_new_thread(printTime, ("Thread-2", 4, ))
except:
  print("无法启动线程")
#startTime = time.time()
while True:
  #endTime = time.time()
  #if endTime - startTime >= 30:
    #_thread.exit()
  pass
