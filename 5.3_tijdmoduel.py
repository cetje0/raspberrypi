#tijdfuncties met time module
import time as time

# huidige tijd
huidige_tijd = time.ctime()
print(huidige_tijd)

#tijd in seconde vanaf 01-01-1970 (unix tijd)
varY = time.time()
print(varY)


# naam van tijdzone
varZ = time.tzname
print(varZ)
