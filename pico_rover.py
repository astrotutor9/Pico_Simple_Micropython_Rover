# A simple coding exercise to build a two wheeled rover using
# a Raspberry Pi Pico in MicroPython.

# import two libraries to access the board and utilise timing
from machine import Pin
from time import sleep

builtinLed = Pin(25, Pin.OUT)

redL = Pin(22,Pin.OUT)
redR = Pin(9, Pin.OUT)

greenL = Pin(21, Pin.OUT)
greenR = Pin(10, Pin.OUT)

blueL = Pin(20, Pin.OUT)
blueR = Pin(11, Pin.OUT)

builtinLed(1)

for flashes in range(4):
    redL(1)
    redR(1)
    sleep(0.5)
    redL(0)
    redR(0)
    greenL(1)
    greenR(1)
    sleep(0.5)
    greenL(0)
    greenR(0)
    blueL(1)
    blueR(1)
    sleep(0.5)
    blueL(0)
    blueR(0)