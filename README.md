# Pico_Simple_Micropython_Rover
 Tutorial on creating a MicroPython rover using the Raspberry Pi Pico.

## Introduction
This is to simply demonstrate utilising the Raspberry Pi Pico pins to control LED and then a rover. Each step will build on the previous giving a result as the code builds up. Take it as far as you like and learn a little along the way. Then when you have completed this take it further!

This will use a Pico, two 400 pin breadboards (though a single 800 will obviously work), LED of various colours, resisters and a button. The rover is a very simple two motor, two wheeled one off eBay with a 4 AA battery box and a Motor Driver Board.

##Initial Code
Open Thonny with a new blank file. On the very bottom right of Thonny click on the text. Select **MicroPython Raspberry Pi Pico**. Select the text again which now should read **Micropython(Raspberry Pi Pico)** and select **Configure Interpreter** at the bottom of the pop up. Then select **Install or update firmware**. Connect your Pico holding down the BootSel button. Ignore the pop folder of the Pico and click Install on the update screen. Close the windows and then as the Thonny editor suggests press Stop button. The MicroPython >>> tab should now show.

In the blank file window add the following code:

```
import machine
import time
```

These two lines will enable you to utilise these libraries. To make use of the parts of them needed you need to call the library into use like this:

```
builtinLed = machine.Pin(25)
```

So machine.Pin would ne needed every time the code required a Pin to be initialised. To circumvent the use of the machine part every time change the two lines of code to:

```
from machine import Pin
from time import sleep
```

Now the machine. can be dropped from the lines of code. Less typing, same result. As a further, I'd suggest unrecommended shortcut, the Pin and sleep could be shortened like this:

```
from machine import Pin as p
from time import sleep as s
```

I wouldn't recommend this as the p and s really do not describe what they are for. Mathematicians use all manner of letters for various things. In software though it makes the code much easier to read if the names are descriptive. This following code would also work:

```
from machine import Pin as Pico_Pin_Number
from time import sleep as Sleeping_Beauty_sleeps_after_biting_the_apple
```

This just demonstrates that it is possible to really personalise your code. If you really want to. For now though let's keep code simple with:

```
from machine import Pin
from time import sleep
```

Now is the time to save the code. Always good to save regulary. Go to File then Save and from the pop-up select **This Computer**. Name your file something like **pico_rover.py** in your folder place of choice. There is no need to save the file to the Pico board yet. The code will run on the board without saving to it. Only when we disconnect the board later from the computer to run on the rover will you have to save onto the Pico. For now it is probably safer to keep it on the hard drive. This is just a recommendation not a rule.

## Make Something Happen
In physical comuting making an LED flash is the Hello World moment. This proves we have control. Add the extra lines to your code.

```
from machine import LED
from time import sleep

builtinLed = Pin(25, Pin.OUT)

# turn on LED for one second, then off
builtinLed(1)
sleep(1)
builtin(0)
```

Press the green arrow button and watch the small LED on the Pico flash on for a second. Just press the arrow again to repeat.

## Adding External LED
The next step is to add an external LED. This will demonstrate control of an external device. If an LED can be lit up then a motor can be turned on. If a motor can be turned on then a rover can move. Simple steps lead to bigger things.

Connect an LED to Pin GP22 following the diagram below. The short leg of the LED links to the resistor and ground, the long leg to GP22 pin of the Pico.

**ADD FRITZING DIAGRAM**

The code now needs to have the new LED added to it. This time there is a small piece repeat using a for loop. The flashes could be anything you like. Blinks, twinkle, toggle, Fido, it doesn't matter. Just choose a wod that means something to you and the code. The range is how many from zero to 4 but not including four. 0, 1, 2, 3 so still four times. Computers count from zero not one. Try changing the (4) to (1,4). This time the range is from one to four. But it doesn't include four so the count is just 1, 2, 3.

```
from machine import Pin
from time import sleep

builtinLed = Pin(25, Pin.OUT)
red1 = Pin(22, Pin.OUT)

# Simple indication to show Pico is powered and script is running
builtinLed(1)

for flashes in range(4):
    red1(1)
    sleep(0.5)
    red1(0)
    sleep(0.5)
```

## Add Some More LED
The next step is to add five more LED. Ideally have three sets of colours as they will be paired later. The LED will represent the connections to the Motor Driver Board of your rover. By switching the LED, the commands will be the same as switching the motors on and off. The same as driving the rover forwards, backwards, left, right or stop. Build your board up as in the diagram. So that the wiring is simpler on the rover use one side of the board for each side of the rover.

**ADD DIAGRAM WITH 6 LED**

The LED names have been changed to indicate the side they are on and the colour. The code for the six led to roll through a dual pattern of flashes is this:

```
# A simple coding exercise to build a two wheeled rover using
# a Raspberry Pi Pico in MicroPython.

# import two libraries to access the board and utilise timing
from machine import Pin
from time import sleep

# Simple indication to show Pico is powered and script is running
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
```

Try changing the sleep values to make the flashes shorter or longer. Change the switching around to create other patterns. Adjust the value of range to make the loop longer if need be.

## Ready for Some Wheel Action

The time has come to add the Pico to the rover. Instead of LED the connections shall be to the Motor Driver Board. The Pico must not be connected directly to any motor. The current draw from the motors is too much. The driverboard switches a more powerful current from commands from the Pico. Keeping the Pico safe.

The connections for the LED are now swapped for connections with the Motor Driver Board. Each connection has a different affect. Each motor has three wires. When the wires are switched live in the correct combination the motor acts in five different ways. The table below should help with this.

|Header | Header | Header |
| ------|--------|--------|
|Line One |Line Two | Line Three |
|Line One |Line Two | Line Three |
