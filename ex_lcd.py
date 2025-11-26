# Préalables
# ----------
# sudo pip3 install adafruit-circuitpython-charlcd --break-system-packages
#
# Connexions
# -------------------------------------------
# #Broche   Fonction                Connexion
# -------   --------                ---------
# 1         VSS - Ground            GND
# 2         VDD - Courant           5V
# 3         V0 - Luminosité         GPIO
# 4         RS - Sélect. registre   GPIO
# 5         RW - Lecture / écrit.   GND
# 6         E - "Enable"            GPIO
# 7         DB0 - Données           --
# 8         DB1 - Données           --
# 9         DB2 - Données           --
# 10        DB3 - Données           --
# 11        DB4 - Données           GPIO
# 12        DB5 - Données           GPIO
# 13        DB6 - Données           GPIO
# 14        DB7 - Données           GPIO

import board
import digitalio
import pigpio
import adafruit_character_lcd.character_lcd as CharLCD
from time import sleep

## board.D1 = GPIO 1, board.D2 = GPIO 2, etc.
## Remplacez "D1" par les valeurs des GPIO qui correspondent à vos connexions
RS = digitalio.DigitalInOut(board.D1)
E = digitalio.DigitalInOut(board.D1)
DB7 = digitalio.DigitalInOut(board.D1)
DB6 = digitalio.DigitalInOut(board.D1)
DB5 = digitalio.DigitalInOut(board.D1)
DB4 = digitalio.DigitalInOut(board.D1)

N_COLS = 8
N_RANGEES = 2
LUMI = 25   # GPIO connecté à V0 qui contrôle la luminosité des pixels affichés

pi = pigpio.pi()
pi.set_mode(LUMI,pigpio.OUTPUT)
lcd = CharLCD.Character_LCD(RS,E,DB4,DB5,DB6,DB7,N_COLS,N_RANGEES)

pi.set_PWM_dutycycle(LUMI,128)  # Contraste des pixels

# Placer au début de la 1ere ligne et afficher un message 1 seconde
lcd.cursor_position(0,0)
lcd.message = "hello"
sleep(1)

# Placer à la fin de la 2e ligne et afficher un message 1 seconde
lcd.cursor_position(5,1)
lcd.message = "bye"
sleep(1)

lcd.clear()
