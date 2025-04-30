import serial
import time
line1 = 0
StatusPWM = 0
# van arduino naar RPI
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            line1 = ser.readline().decode('utf-8').rstrip()
            print(line1)
        StatusPWM = int((line1/50)*255)

        
        ser.write(StatusPWM)
        line2 = ser.readline().decode('utf-8').rstrip()
        print(line2)
        time.sleep(1)