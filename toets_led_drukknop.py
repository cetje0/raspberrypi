from gpiozero import LED, Button # van module gpoizero importeer LED en BUTTON
from time import sleep # van module time importeer sleep

knop = Button(17, pull_up = 0) # var knop in BUTTON op gpioPin 17 met pull_up false
varLED_auto_rood = LED(14) # varLED_auto_rood = LED op gpioPin 14
varLED_auto_oranje = LED(15) # varLED_auto_oranje = LED op gpioPin 15
varLED_auto_groen = LED(18) # varLED_auto_groen = LED op gpioPin 18
varLED_voetganger_rood = LED(23) # varLED_voetganger_rood = LED op gpioPin 23
varLED_voetganger_groen = LED(24) # varLED_voetganger_groen = LED op gpioPin 24

while True: # loop opstellen
    if varLED_voetganger_rood.on() and varLED_auto_groen.on():
        sleep(10)

    if (knop.value %2 == 1): # als de module van de waarde gelijk is aan 1
        varLED_auto_groen.off() # varLED_auto_groen laag.
        varLED_auto_oranje.on() # varLED_auto_oranje hoog
        varLED_voetganger_rood.on() # varLED_voetganger_rood hoog
        sleep(2) # wacht 10 seconde
        varLED_auto_oranje.off() # varLED_auto_oranje laag
        varLED_auto_rood.on() # varLED_auto_rood hoog
        varLED_voetganger_groen.on() # varLED_voetganger_groen hoog
        varLED_voetganger_rood.off() # varLED_voetganger_rood laag
        sleep(5) # wacht 2 minuten
        varLED_voetganger_rood.on() # varLED_voetganger_rood hoog
        varLED_voetganger_groen.off() # varLED_voetganger_groen laag
        varLED_auto_rood.off() # varLED_auto_rood laag
        
    else: # anders 
        varLED_auto_groen.on() # varLED_auto_groen hoog
        varLED_voetganger_rood.on() # varLED_voetganger_rood hoog
    


        
