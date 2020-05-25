#server
import socket
import numpy
import array
import wave
import struct
import _thread
import time

def wavSetOyt(outAbsPath, pcmArray, pcmRate):
  #先创建准备写入的WAVE文件
  waveF = wave.open(outAbsPath, "wb")
  #设置声道数
  waveF.setnchannels(1)
  #设置多少BT记录，我们一般16bit=2byte
  waveF.setsampwidth(2)
  #设置采样率
  waveF.setframerate(pcmRate)
  for val in pcmArray:
    #float 转为int
    print(val)
    val = round(float(val))
    dataStruct = struct.pack("<h", val)
    waveF.writeframesraw(dataStruct)
  waveF.writeframesraw(b"")
  waveF.close()

def tcplink(conn, addr):
  recvAll = b""
  while 1:
    data = conn.recv(1000)
    if not data:
      break

    recvAll += data
    if len(recvAll) < 32002:
      continue
    
    #开始转换
    recvArray = numpy.frombuffer(recvAll[0:32002], "uint16")
    rate = recvArray[16000]
    pcmData12Bit = recvArray[0:16000]
    """
    12bit uint的数组拉伸到16bit，再转到-32767-32868
    """
    #用float32去保存
    pcmDataU12bit_f = pcmData12Bit.astype(numpy.float32)
    #把12bit的采样数据拉伸到16bit
    pcmDataU16bit_f = pcmDataU12bit_f * 16
    #转为-32768 - 32767 < 正规pcm数据
    pcmData16bit_f = pcmDataU16bit_f - 32768

    tick = str(int(time.time()))
    outPath = "/opt/code/pythonCode/voice/background/"+ tick  +".wav"
    wavSetOyt(outPath, pcmData16bit_f, rate)
    print(addr)

  conn.close()

sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_tcp.bind(("0.0.0.0", 8000))
sock_tcp.listen(100)
while 1:
  print("listening")
  conn, addr = sock_tcp.accept()
  _thread.start_new_thread(tcplink, (conn, addr))
