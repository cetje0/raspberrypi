import gpiozero as io
import time as t

sensor1 = io.DistanceSensor(echo = 18,  trigger = 17) # 18 = echo   17 = trig

while True:
    print(f"afstand van sensor 1 :{sensor1.distance * 100}")
    t.sleep(2)

