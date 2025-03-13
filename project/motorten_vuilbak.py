import gpiozero as io
from time import sleep
uitkomst = ""
servo_draaien = io.AngularServo(17, min_angle = 0, max_angle = 360)
servo_duwen = io.AngularServo(21, min_angle = 0, max_angle = 360)
while True:
    if uitkomst == "rest":
        servo_draaien.angle = 0
        sleep(1)
        servo_duwen.angle = 360
        sleep(0.5)
        servo_duwen.angle = 0
    elif uitkomst == "pmd":
        servo_draaien.angle = 90
        sleep(1)
        servo_duwen.angle = 360
        sleep(0.5)
        servo_duwen.angle = 0
    elif uitkomst == "gft":
        servo_draaien.angle = 180
        sleep(1)
        servo_duwen.angle = 360
        sleep(0.5)
        servo_duwen.angle = 0
