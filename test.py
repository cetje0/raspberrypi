import gpiozero as io
from time import sleep

led = io.PWMLED(2)

for b in range(101):
    led.value = b/100.0
    print(led.value)
    sleep(0.01)
