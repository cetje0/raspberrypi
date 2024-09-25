from gpiozero import LED, Button
from time import sleep

knop = Button(17, pull_up = 0)
varLED = LED(18)
teller = 0

while True:
    print(knop.value)
    if teller%2 == 0:
       varLED.on()
       teller+=1
    else :
        varLED.off()
