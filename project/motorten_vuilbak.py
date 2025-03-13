import gpiozero as io

uitkomst = ""
servo_draaien = io.AngularServo(17, min_angle = 0, max_angle = 360)
if 