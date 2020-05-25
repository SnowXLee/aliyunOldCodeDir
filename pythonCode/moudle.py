import time
gg = 'a'
def areyouok(request):
  if request == 'are you ok?':
    ticks = time.time()
    print(ticks)
    response = "i'm find thank you."
  return response
