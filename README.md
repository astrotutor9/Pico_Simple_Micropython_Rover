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

##Adding External LED
The next step is to 
