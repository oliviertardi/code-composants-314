import pigpio
import time

BUZ = 21

pi = pigpio.pi()
pi.set_mode(BUZ, pigpio.OUTPUT)

# Changer la valeur du délai change la hauteur du son
delai = 1

try:
    while True:
        pi.write(BUZ,1)
        time.sleep(delai)
        pi.write(BUZ,0)

except KeyboardInterrupt:
    pi.write(BUZ,0)