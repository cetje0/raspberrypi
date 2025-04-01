import gpiozero as io#importeer gpiozero als io
from RpiMotorLib import RpiMotorLib#importeer RpiMotorLib
import time as time#importeer time als time
knop_verhogen = io.Button(16, pull_up = 0)# de pin van var knop_verhogen is 16
knop_verminderen = io.Button(20, pull_up = 0)# de pin van var knop_verminderen is 20
knop_ack = io.Button(21, pull_up = 0)# de pin van var knop_ack is 21
instelling = 0# var instelling is 0
waarde_instellingen = -75# var waarde_instelling is -75
vorige_waarde = -150# var vorige_waarde is -150
while True:#whileloop opstellen
    stappen_motor = RpiMotorLib.BYJMotor("BYJmotorX", "28BYJ")# var stapppen_motor is RpiMotorLib.BYJMotor("BYJmotorX", "28BYJ")
    stap_motor_pins = [18,23,24,25]# var stap_motor_pins zijn 18,23,24,25
    if knop_verhogen.is_active:#als var knop_verhogen actief is 
        if instelling != 6:# als var instell!ing niet 6 is
            instelling +=1 # var instelling +1 met zichzelf
            waarde_instellingen +=75# var waarde_instellingen +75 met zichzelf
            vorige_waarde += 75# var vorige_waarde +75 met zichzelf
            print(instelling, waarde_instellingen)#print instelling, waarde_instellingen
            time.sleep(0.5)# wacht
    stappen = (waarde_instellingen/360)*512
    vorige_stap = (vorige_waarde/360)*512
    if instelling == 1 and knop_ack.is_active:
        print(stappen,vorige_stap)
        stappen_motor.motor_run(stap_motor_pins, 0.003,stappen,False,False,"full", 0.05)
    elif instelling == 2 and knop_ack.is_active:
        print(stappen,vorige_stap)
        stappen_motor.motor_run(stap_motor_pins, 0.003,stappen-vorige_stap,False,False,"full", 0.05)
    elif instelling == 3 and knop_ack.is_active:
        print(stappen,vorige_stap)
        stappen_motor.motor_run(stap_motor_pins, 0.003,stappen-vorige_stap,False,False,"full", 0.05)
    elif instelling == 4 and knop_ack.is_active:
        print(stappen,vorige_stap)
        stappen_motor.motor_run(stap_motor_pins, 0.003,stappen-vorige_stap,False,False,"full", 0.05)
    elif instelling == 5 and knop_ack.is_active:
        print(stappen,vorige_stap)
        stappen_motor.motor_run(stap_motor_pins, 0.003,stappen-vorige_stap,False,False,"full", 0.05)
    
    if knop_verminderen.is_active:
        if instelling != 0:
            instelling -=1
            waarde_instellingen -=75
            vorige_waarde -= 75
        print(instelling, waarde_instellingen)
        time.sleep(0.5)
    if instelling == 1 and knop_ack.is_active:
        print(stappen,vorige_stap)
        stappen_motor.motor_run(stap_motor_pins, 0.003,stappen,True,False,"full", 0.05)
    elif instelling == 2 and knop_ack.is_active:
        print(stappen,vorige_stap)
        stappen_motor.motor_run(stap_motor_pins, 0.003,stappen-vorige_stap,True,False,"full", 0.05)
    elif instelling == 3 and knop_ack.is_active:
        print(stappen,vorige_stap)
        stappen_motor.motor_run(stap_motor_pins, 0.003,stappen-vorige_stap,True,False,"full", 0.05)
    elif instelling == 4 and knop_ack.is_active:
        print(stappen,vorige_stap)
        stappen_motor.motor_run(stap_motor_pins, 0.003,stappen-vorige_stap,True,False,"full", 0.05)
    elif instelling == 5 and knop_ack.is_active:
        print(stappen,vorige_stap)
        stappen_motor.motor_run(stap_motor_pins, 0.003,stappen-vorige_stap,True,False,"full", 0.05)
    