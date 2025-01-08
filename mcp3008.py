""" #from gpiozero import MCP3008
#import time

LDR = MCP3008(channel = 0)
while True:
    licht = LDR.value
    print(licht)
    time.sleep(1) """

from gpiozero import PWMLED, MCP3008
import time

pot = MCP3008(0)
led = PWMLED(14)

while True:
    if(pot.value < 0.001):
        led.value = 0
    else:
        led.value = pot.value
    print(pot.value)
    time.sleep(0.1)
    