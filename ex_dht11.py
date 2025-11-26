# Prérequis
# pip3 install adafruit-circuitpython-dht --break-system-packages

import board
import time
import adafruit_dht

# À l'initialisation il faut donner le port GPIO (board.DXX) 
# où la broche S du senseur est connectée
dht11 = adafruit_dht.DHT11(board.D21)

# Boucle principale
try:
    while True:
        print("Temp:",dht11.temperature)
        print("Hum: ",dht11.humidity)
        print()
        time.sleep(1)

except KeyboardInterrupt:
    print("Programme interrompu.")