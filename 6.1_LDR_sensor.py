# LDR meet licht en donker
from gpiozero import LightSensor

varSensor = LightSensor(18)

while True:
    print(varSensor.value)
    varSensor.wait_for_light()
    print("er is licht")
    varSensor.wait_for_dark()
    print("het is donker")
