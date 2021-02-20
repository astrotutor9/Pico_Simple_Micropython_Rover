# A simple coding exercise to build a two wheeled rover using
# a Raspberry Pi Pico in MicroPython.

# import two libraries to access the board and utilise timing
from machine import Pin
from time import sleep
from random import randint

# Set up definitions of pins being used
builtinLed = Pin(25, Pin.OUT)

enable_L = Pin(22,Pin.OUT)
enable_R = Pin(9, Pin.OUT)

forward_L = Pin(21, Pin.OUT)
forward_R = Pin(10, Pin.OUT)

reverse_L = Pin(20, Pin.OUT)
reverse_R = Pin(11, Pin.OUT)

button = Pin(14, Pin.IN)

# define switch pressed or not pressed
button_pressed = False

# define left motor going forwards
def left_forwards():
    enable_L(1)
    forward_L(1)
    reverse_L(0)
    
# define left motor going backwards
def left_reverse():
    enable_L(1)
    forward_L(0)
    reverse_L(1)

# define right motor going forwards
def right_forwards():
    enable_R(1)
    forward_R(1)
    reverse_R(0)
    
    # define right motor going backwards
def right_reverse():
    enable_R(1)
    forward_R(0)
    reverse_R(1)

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
    
def rover_reverse():
    left_reverse()
    right_reverse()

# define both motors to stop
def rover_stop():
    left_stop()
    right_stop()

# define a right turn
def right_turn():
    left_forwards()
    right_reverse()

# define a left turn
def left_turn():
    left_reverse()
    right_forwards()
    

# set up empty list for movement sequence
movement = []

while button_pressed != True:
    if button.value() == 1:
        print("Pressed")
        button_pressed = True
        builtinLed(1)
        for move in range(10):
            movement.append(randint(1, 5))
        sleep(2)
        builtinLed(0)

for moves in movement:
    if moves == 1:
        rover_forwards()
        print("Forwards")
        sleep(1)
    elif moves == 2:
        rover_reverse()
        print("Reverse")
        sleep(1)
    elif moves == 3:
        right_turn()
        print("Right")
        sleep(0.6)
    elif moves == 4:
        left_turn()
        print("Left")
        sleep(0.6)

rover_stop()
print("Rover stopped")