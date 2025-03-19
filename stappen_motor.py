import gpiozero as io
from RpiMotorLib import RpiMotorLib
while True:
    afstand_in_mm = int(input(f"Welke afstand wiltu afleggen(mm) ?"))
    stappen_motor = RpiMotorLib.BYJMotor("BYJmotorX", "28BYJ")
    stappen = abs((afstand_in_mm / 7)*512)
    stap_motor_pins = [18,23,24,25]
    if afstand_in_mm < 0:
        stappen_motor.motor_run(stap_motor_pins, 0.003,stappen,True,False,"full", 0.05)
    else:
        stappen_motor.motor_run(stap_motor_pins, 0.003, stappen, False, False,"full",0.05)

