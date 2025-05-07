""" import time 
from smbus2 import SMBus
from bmp280 import BMP280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

print(""" "temperatuur-and-druk.py - display the temp and druk."
"press crl +C to exit"
""")
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

while True:
    temp = bmp280.get_temperature()
    druk = bmp280.get_pressure()
    print(f"{temp:05.2f}*C {druk:05.2f}hPa")
    time.sleep(1)      """
