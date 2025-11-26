# Exemple de code pour le détecteur de distance HC-SR04
# 
# Connexions:
# VCC   -   5V
# Trig  -   GPIO
# Echo  -   GPIO
# GND   -   GND

import pigpio
import time

TRIG = 21
ECHO = 20
V_SON = 343 # Vitesse du son 343 m/s

pi = pigpio.pi()
pi.set_mode(TRIG,pigpio.OUTPUT)
pi.set_mode(ECHO,pigpio.INPUT)
pi.write(TRIG,0)

try:
    while True:
        
        # Envoyer l'ultrason
        pi.write(TRIG,1)
        time.sleep(0.00001)
        pi.write(TRIG,0)

        # Attendre l'echo
        while pi.read(ECHO) == 0: pass
        debut_signal = time.time()

        # Attendre la fin de l'echo
        while pi.read(ECHO) == 1: pass
        fin_signal = time.time()

        # Calculer le distance
        # On divise par 2 car le son fait 2x la distance (aller-retour)
        duree_signal = fin_signal - debut_signal
        distance = duree_signal * V_SON / 2 

        print(distance)

        time.sleep(1)

except KeyboardInterrupt:
    pi.stop()

