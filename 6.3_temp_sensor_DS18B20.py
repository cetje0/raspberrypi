import time
from w1thermsensor import W1ThermSensor
sensor=W1ThermSensor()
while True:
    temperatuur = sensor.get_temperature()
    print(f"De temperatuur in graden celsius is nu {temperatuur}")
    time.sleep(1)
