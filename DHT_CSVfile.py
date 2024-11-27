import board # importeer board
import adafruit_dht # importeer adafruit_dht
from time import sleep, strftime # van module time importeer sleep en strftime

dht11_1 = adafruit_dht.DHT11(board.D18) # var dht11_1 staat op pin 18
dht11_2 = adafruit_dht.DHT11(board.D23) # var dht11_2 staat op pin 23

with open("eggs.csv", "a") as csvfile:# open csv tekst bestand
    while True:# stel while loop op
        sleep(3)# wacht 3 seconde
        try:# probeer
            temp_dht11_1 = dht11_1.temperature # var temp_dht11_1 is temperatuur opvragen van dht11
            temp_dht11_2 = dht11_2.temperature # var temp_dht11_2 is temperatuur opvragen van dht11
        except RuntimeError as error:# alleen error code
            print(error.args[0])# print de error
            continue# ga verder
        gemiddelde = (temp_dht11_1 + temp_dht11_2) /2 # var gemiddelde is de 2 temperaturen van de dht's optellen en gedeelt door 2
        print(gemiddelde)
        csvfile.write("{0}, {1}, {2}, {3}\n".format(strftime("%Y-%m-%d %H:%M:%s"), temp_dht11_1,  temp_dht11_2,  gemiddelde))# schrijf in csv time stap en var temp_dht11_1, temp_dht11_2,  gemiddelde 