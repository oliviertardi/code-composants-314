# Préalables
# sudo pip3 install adafruit-circuitpython-irremote --break-system-packages
# 
# Référence
# https://docs.circuitpython.org/projects/irremote/en/latest/
#
# La communication IR fonctionne par pulsations, à la manière du code Morse
# mais pour des valeurs binaires. Par exemple, le nombre 37 vaut 00100101 en
# binaire: pour transmettre ce nombre, on enverrait une série d'impulsions 
# où les courtes = 0 et les longues = 1.
# Le module pulseio permet d'accéder à ces pulsations; le module adafruit_irremote
# permet de les décoder
 
import pulseio
import board
from adafruit_irremote import GenericDecode, IRDecodeException

# Remplacez ici "D21" par le numero du GPIO où est connecté le module IR
puls = pulseio.PulseIn(board.D21, maxlen=200, idle_state=True)
decodeur = GenericDecode()

try:
    while True:
        message = decodeur.read_pulses(puls)
        code = decodeur.decode_bits(message)
        print(code[0]) 

except IRDecodeException:     
    print("Code inconnu.")
except KeyboardInterrupt:
    print("Terminé.")

