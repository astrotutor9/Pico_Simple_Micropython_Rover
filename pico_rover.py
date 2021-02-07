# A simple coding exercise to build a two wheeled rover using
# a Raspberry Pi Pico in MicroPython.

# import two libraries to access the board and utilise timing
from machine import Pin
from time import sleep

builtinLed = Pin(25, Pin.OUT)

builtinLed(1)

for flashes in range(4):
    red1(1)
    sleep(0.5)
    red1(0)
    sleep(0.5)