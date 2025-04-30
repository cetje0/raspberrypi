from gpiozero import Motor,MCP3008
import time


pot = MCP3008(0)
motor = Motor(17, 18 )
snelheid_motor = 0
while True:
    motor.forward()
    print("okay")
    time.sleep(1)
