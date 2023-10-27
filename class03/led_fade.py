import os, sys, io
import M5
from M5 import *
from hardware import *


pin1 = None
pin2 = None


def setup():
  global pin1, pin2

  M5.begin()
  pin1 = Pin(1, mode=Pin.OUT)
  pin2 = Pin(2, mode=Pin.IN)
  rgb= RGB (IO=2, N=10, TYPE="WS2812")

def loop():
  global rgb, state
  M5.update()
  if(input_pin.value())
    state = 'red'
    print('change to', state)
    time.sleep(1)
  else:
      for i in range (100):
          rgb.fill_color(get_color(0, i, 0))
          time.sleep_ms(20)
  elif(state =='red'):
      if(input_pin.value())
        state = 'green'

if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")