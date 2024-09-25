from time import sleep
from gpiozero import LED
import random

varLed_blauw = LED(14)
varLed_groen = LED(23)
varLed_rood = LED(18)

while True:
    status_rood = random.randint(0,1)
    status_groen = random.randint(0,1)
    status_blauw = random.randint(0,1)
    sleep(0.5)
    if (status_rood == 0) and (status_groen == 0) and (status_blauw == 0):
        varLed_blauw.off()
        varLed_groen.off()
        varLed_rood.off()
    elif (status_rood == 1):
        varLed_rood.on()
        print(f"rood = {status_rood}")
    elif(status_groen == 1):
        varLed_groen.on()
        print(f"groen = {status_groen}")
    elif (status_blauw == 1):
        varLed_blauw.on()
        print(f"blauw = {status_blauw}")
    