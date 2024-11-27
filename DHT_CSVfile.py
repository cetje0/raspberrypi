import board
import adafruit_dht 
from time import sleep, strftime

dht11_1 = adafruit_dht.DHT11(board.D18)
dht11_2 = adafruit_dht.DHT11(board.D23)

with open("eggs.csv", "a") as csvfile:
    while True:
        sleep(3)
        try:
            temp_dht11_1 = dht11_1.temperature
            temp_dht11_2 = dht11_2.temperature
        except RuntimeError as error:
            print(error.args[0])
            continue
        gemiddelde = (temp_dht11_1 + temp_dht11_2) //2
        print(gemiddelde)
        csvfile.write("{0}, {1}, {2}, {3}\n".format(strftime("%Y-%m-%d %H:%M:%s"), temp_dht11_1,  temp_dht11_2,  gemiddelde))