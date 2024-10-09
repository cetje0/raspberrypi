# button op GPIO04
import gpiozero as io 
from time import sleep

knop = io.Button(18, pull_up = 0, )
varLED_1 = io.LED(21)


while True:
    sleep(0.1)
    if knop.value:
        print("Button is ingedrukt")
        
        
        varLED_1.on()
    else: 
        print("Button is niet ingedrukt")
        varLED_1.off()
