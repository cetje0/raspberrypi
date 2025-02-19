import board # importeer board
import adafruit_dht # importeer adafruit_dht
import time
import gpiozero as io

dhtDevice = adafruit_dht.DHT11(board.D18)
pwm_motor = io.PWMOutputDevice(22)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
                temperature_c, humidity
            )
        )
        pwm_temp = 6.67 * temperature_c - 100
        pwm_hum = 2.22 * humidity - 55.56
        pwm_motor = (max(pwm_temp, pwm_hum))
    
        time.sleep(2.0)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    
