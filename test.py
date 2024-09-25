from time import sleep
from gpiozero import LED

varLed_1 = LED(18)
varLed_2 = LED(23)

while True:
    varLed_1.on()
    varLed_2.off()
    sleep(1)
    varLed_1.off()
    varLed_2.on()
    sleep(1)
