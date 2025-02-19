import time
from gpiozero import RGBLED
import adafruit_dht, board

RGB_waardes = [[255,0,0],
               [205,38,38],
               [205,55,0],
               [250,128,114],
               [238,149,114],
               [255,127,0],
               [205,133,0],
               [238,173,14],
               [238,221,130],
               [205,205,0],
               [255,246,143],
               [124,252,0],
               [0,255,0],
               [78,238,148],
               [0,245,255],
               [151,255,255],
               [0,255,255],
               [135,206,250],
               [30,144,255],
               [0,0,255]]

DHT11_pin = adafruit_dht.DHT11(board.D18)
rgb_led = RGBLED(5,6,13)                   

while True:
    try:
        temperatuur = DHT11_pin.temperature
        berekening_eerste_index = temperatuur//2
        rgb_led.color = (RGB_waardes[berekening_eerste_index][0]/255,RGB_waardes[berekening_eerste_index][1]/255,RGB_waardes[berekening_eerste_index][2]/255)
        print(f"temp is {temperatuur}")
        print(f"berekening is {berekening_eerste_index}")
        time.sleep(1)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        DHT11_pin.exit()
        raise error
    time.sleep(2)
