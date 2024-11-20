#druk start 2 rode ledjes aan tussen 2 en  10 seconden geeft rpi start 2 drukkenknoppen wie het eerste drukt blijft de led 
#aan en van de andere gaat de led uit en kan niet meer aan tot start gedrukt
import gpiozero as io # importeer gpiozero als io
import time as t # importeer tiem als t
import random # importeer random



start = io.Button(14, pull_up= 0) # start is gpiobutton 14 met pull down
spel_status = 0 # var spel_status is nul
speler1 = io.Button(15, pull_up= 0)# speler1 is gpiobutton 15 met pull down
speler2 = io.Button(18, pull_up= 0)# speler2 is gpiobutton 18 met pull down
speler1_varLed1 = io.LED(23) # speler1_varLed1 is gpioLED 23
speler2_varLed2 = io.LED(24) # speler2_varLed2 is gpioLED 24
speler1_status = 0 # var speler1_status is nul
speler2_status = 0 # var speler2_status is nul


while True:# stel while loop op
    if start.value and spel_status == 0: # als start knop waarde 1 is en spel_status is nul
        speler1_status = 0# speler1_status is nul
        speler2_status = 0# speler2_status is nul
        speler1_varLed1.on()# LED speler1 aan
        speler2_varLed2.on()# LED speler2 aan
        tijd = random.randint(2, 10) # var tijd is random waarde tussen 2 en 10 seconde
        t.sleep(tijd)# wacht var tijd
        print("start")# print start
        spel_status = 1# var spel_status is 1

    if spel_status:# als spel_status 1 is 
       
        if speler1.value:# als speler1 drukt
            speler1_status = 1# speler1_status is 1

        if speler2.value:# als speler2 drukt
            speler2_status = 1# speler2_status is 2

        if speler1_status == 1:# als speler1_status gelijk is aan 1
            speler1_varLed1.on()# LED speler1 aan
            speler2_varLed2.off()# LED speler2 uit
            print("speler1 wint")# print speler1 wint
            spel_status = 0 # spel_status is 0

        if speler2_status == 1:# als speler2_status gelijk is aan 1
            speler2_varLed2.on()# LED speler2 aan
            speler1_varLed1.off()# LED speler1 uit
            print("speler2 wint")# print speler2 wint
            spel_status = 0# spel_status is 0