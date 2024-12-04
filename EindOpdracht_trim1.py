import gpiozero as io
import time as t

led1_groen = io.LED(21)
led2_groen = io.LED(20)
led1_oranje = io.LED(16)
led2_oranje = io.LED(12)
led1_rood = io.LED(7)
led2_rood = io.LED(8)
sensor1 = io.DistanceSensor(18, 17) # 18 = echo   17 = trigger
sensor2 = io.DistanceSensor(13, 19) # 5 = echo  6 = trigger
gemiddelde = 0

while True:
    print(f"afstand sensor 1 :{sensor1.distance * 100}")

    print(f"afstand sensor2: {sensor2.distance * 100} ")

    gemiddelde = (sensor1.distance + sensor2.distance /2)*100


    if gemiddelde <= 5:
        led1_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led2_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led1_oranje.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led2_oranje.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led1_rood.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led2_rood.blink(on_time=0.500, off_time=0.500, n = None, background = True)

    elif gemiddelde <= 10:
        led1_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led2_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led1_oranje.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led2_oranje.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led1_rood.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led2_rood.blink(on_time=0.500, off_time=0.500, n = None, background = True)

    elif gemiddelde <= 20:
        led2_rood.off()

        led1_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led2_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led1_oranje.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led2_oranje.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led1_rood.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        
    elif gemiddelde <= 30:
        led1_rood.off()
        led2_rood.off()

        led1_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led2_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led1_oranje.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led2_oranje.blink(on_time=0.500, off_time=0.500, n = None, background = True)

    elif gemiddelde <= 40:
        led2_oranje.off()
        led1_rood.off()
        led2_rood.off()

        led1_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led2_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led1_oranje.blink(on_time=0.500, off_time=0.500, n = None, background = True)

    elif gemiddelde <= 50:
        led1_oranje.off()
        led2_oranje.off()
        led1_rood.off()
        led2_rood.off()

        led1_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)
        led2_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)

    elif gemiddelde <= 60:
        led1_oranje.off()
        led2_oranje.off()
        led1_rood.off()
        led2_rood.off()
        led2_groen.off()

        led1_groen.blink(on_time=0.500, off_time=0.500, n = None, background = True)





