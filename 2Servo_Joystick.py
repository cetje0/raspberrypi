from re import X
from gpiozero import AngularServo, MCP3008
from time import sleep
servo_x = AngularServo(17, min_angle = 0, max_angle=180)
servo_y = AngularServo(21, min_angle=0, max_angle=180)
x_as = MCP3008(channel=0)
y_as = MCP3008(channel=1)

while True:
    servo_x.angle = x_as.value * 180
    servo_y.angle = y_as.value * 180
    sleep(0.5)