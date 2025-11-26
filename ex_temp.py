import busio
import board
from math import log

from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn


# Initialisations
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)
data = AnalogIn(ads, 0)


# Boucle principale
try:
    while True:
        print(data.value,data.voltage)
        # Calcul de la temperature à partir de la resistance
        v=(data.value/32767)*5
        r=(5-v)/v*4700
        t = 1/(  log(r/10000) /3950 + 1/(25+273.15))-273.15
        print(t);

except KeyboardInterrupt:
    print("Programme interrompu.")