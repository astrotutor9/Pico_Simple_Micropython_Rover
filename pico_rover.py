# A simple coding exercise to build a two wheeled rover using
# a Raspberry Pi Pico in MicroPython.

# import two libraries to access the board and utilise timing
from machine import Pin
from time import sleep

# Simple indication to show Pico is powered and script is running
builtinLed = Pin(25, Pin.OUT)

enable_L = Pin(22,Pin.OUT)
enable_R = Pin(9, Pin.OUT)

forward_L = Pin(21, Pin.OUT)
forward_R = Pin(10, Pin.OUT)

reverse_L = Pin(20, Pin.OUT)
reverse_R = Pin(11, Pin.OUT)

# Simple indication to show Pico is powered and script is running
builtinLed(1)

# define left motor going forwards
def left_forwards():
    enable_L(1)
    forward_L(1)
    reverse_L(0)

# define right motor going forwards
def right_forwards():
    enable_R(1)
    forward_R(1)
    reverse_R(0)

# define left motor to stop
def left_stop():
    enable_L(1)
    forward_L(0)
    reverse_L(0)

# define right motor to stop
def right_stop():
    enable_R(1)
    forward_R(0)
    reverse_R(0)

# define both motors to go forwards
def rover_forwards():
    left_forwards()
    right_forwards()

# define both motors to stop
def rover_stop():
    left_stop()
    right_stop()
    
rover_forwards()  # go forwards
sleep(5)          # for 5 seconds
rover_stop()      # then stop