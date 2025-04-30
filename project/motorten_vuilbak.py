import gpiozero as io
from time import sleep
uitkomst = "pmd"
servo_draaien = io.AngularServo(20, min_angle = -90, max_angle = 90)
servo_duwen = io.AngularServo(16, min_angle = 0, max_angle = 180)
""" " ""   if uitkomst == "'rest'":
        servo_draaien.angle = 0
        print("okay")
        sleep(1)
        servo_duwen.angle = 360
        sleep(0.5)
        servo_duwen.angle = 0
            elif uitkomst == "gft":
        servo_draaien.angle = 180
        print("okay")
        sleep(1)
        servo_duwen.angle = 360
        sleep(0.5)
        servo_duwen.angle = 0"""""" """
while True:
    servo_draaien.angle = -90
    sleep(2)
    servo_draaien.angle = -45
    sleep(2)
    servo_draaien.angle = 0
    sleep(2)
    servo_draaien.angle = 45
    sleep(2)
    servo_draaien.angle = 90
    sleep(2)

