from gpiozero import MCP3008, PWMLED
import time

led = PWMLED(14)
verschill  =0
vorige_temp1 = 0
vorige_temp2 =0
huidige_tijd = time.ctime()

def convert_temp1(gen1):
    for value1 in gen1:
        yield round((value1 *3.3-0.5)*100, 0)
def convert_temp2(gen2):
    for value2 in gen2:
        yield round((value2 *3.3-0.5)*100, 0)

f = open("tmp_waardes", "w")
f.write(f"{huidige_tijd}\n")
f.close()

mcp3008_kanaal1 = MCP3008(channel=0)
mcp3008_kanaal2 = MCP3008(channel=1)
while True:
    for temp1 in convert_temp1(mcp3008_kanaal1.values):
        print(f"de temperatuur is {temp1} C")
        time.sleep(1)
        break

    for temp2 in convert_temp2(mcp3008_kanaal2.values):
        print(f"tmp2 = {temp2}C")
        time.sleep(1)
        break

    if vorige_temp1 != temp1 or vorige_temp2 != temp2:
        f = open("tmp_waardes", "a")
        f.write(f"{huidige_tijd}")
        f.write(f"temperatuur van eerste tmp is veranderd: {temp1}, temperatuur van tweede is veranderd: {temp2}\n")
        f.close()
        vorige_temp1 = temp1
        vorige_temp2 = temp2


    verschill = round(abs(temp1 - temp2), 1)
    if verschill > 2:
        led.blink(on_time=0.500, off_time=0.500, n = None, background = True)
    else:
        led.off()