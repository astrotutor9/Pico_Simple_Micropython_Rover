# A simple coding exercise to build a two wheeled rover using
# a Raspberry Pi Pico in MicroPython.

# import two libraries to access the board and utilise timing
from machine import Pin
from time import sleep

builtinLed = Pin(25, Pin.OUT)
builtinLed(1)
sleep(1)
builtinLed(0)