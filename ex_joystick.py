# Le joystick doit être connecté sur le convertisseur analogue-digital
# chacun des axes doit avoir son propre canal, par exemple A0 et A1
# Les valeurs lues sont entre :
#  0 - 32767 (5V)
#  0 - 26250 environ (3.3V)
# Attention, lorsque le joystick est au milieu, la valeur lue n'est
# pas exactement à la moitié de ces limites
 
import busio
import board
import time
import pigpio

from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

# Initialisations
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)
data_x = AnalogIn(ads, 0)
data_y = AnalogIn(ads, 1)

# Boucle principale
try:
    while True:
        print("x:",data_x.value,"y:",data_y.value)

except KeyboardInterrupt:
    print("Programme interrompu.")