from gpiozero import LED, Button
from time import sleep

knop = Button(18, pull_up = 0)
varLED = LED(24)
teller = 0

while True:
    if knop.is_pressed:
        teller += 1
        sleep(1)
    if teller%2 == 0:
       varLED.on()
       print(teller)
    else :
        varLED.off()
