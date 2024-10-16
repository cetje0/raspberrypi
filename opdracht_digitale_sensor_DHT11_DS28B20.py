import time
from w1thermsensor import W1ThermSensor
import board
import adafruit_dht
import gpiozero as io

dht11 = adafruit_dht.DHT11(board.D18)
sensor=W1ThermSensor() # sensor pin op 4
var_LED_rood = io.LED(26)
f = open("gemiddelde_temperatuur.txt", "w")
gemiddelde = 0

while True:
    DS18B20_c = round(sensor.get_temperature(), 0)
    temp_dht11 = dht11.temperature
    varX = time.ctime()

    print(f"temperatuur van DS18B20 {DS18B20_c}")
    print(f"temperatuur van DHT11 {temp_dht11}")

    gemiddelde = (DS18B20_c + temp_dht11) /2


    if (abs(DS18B20_c - temp_dht11 > 5)):
        var_LED_rood.on()
        f = open("gemiddelde_temperatuur.txt", "a")
        f.write(f"{varX}:  temperatuurverschil is te hoog, check de sensor.\n")
        f.close()
    else:
        var_LED_rood.off()
        f = open("gemiddelde_temperatuur.txt", "a")
        f.write(f"{varX}:  gemiddelde temp is: {gemiddelde} \n")
        f.close()
    time.sleep(1)
