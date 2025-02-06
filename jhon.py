from time import sleep
from gpiozero import MCP3008, PWMOutputDevice, DigitalOutputDevice, Button

potmeter = MCP3008(0)
motorcheck = PWMOutputDevice(22)
motorR = DigitalOutputDevice(17)
motorL = DigitalOutputDevice(27)
knop = Button(4)

motorR.on()
motorL.off()

try:
    while True:
        potmeterWaarde = potmeter.value 
        motorcheck.value =potmeterWaarde
        
        print(f"potmeter: {potmeterWaarde}")
        print(f"motorwaarde: {motorcheck.value}")
        print(" ")
        sleep(1)
        
except KeyboardInterrupt:
    print("stop")
    motorcheck.off()