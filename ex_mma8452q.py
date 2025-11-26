# https://github.com/ControlEverythingCommunity/MMA8452Q/tree/master/Python
# 
import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# INITIALISATION + CONFIGURATION
# ------------------------------
# La méthode bus_write_byte_data() a 3 arguments:
# - L'adresse du composant i2c. On peut la trouver avec la commande linux 'i2cdetect -y 1'
# - L'adresse du registre où écrire
# - La valeur à écrire
# Voir la documentation pour les instructions possibles
# https://www.nxp.com/docs/en/data-sheet/MMA8452Q.pdf

# Initialiser =  Écrire 0 à l'adresse 0x2A
bus.write_byte_data(0x1D, 0x2A, 0x00)

# Activer = Écrire 1 à l'adresse 0x2A
bus.write_byte_data(0x1D, 0x2A, 0x01)

# Donner la valeur de configuration par défaut = écrire 0 à l'adresse 0x0E
bus.write_byte_data(0x1D, 0x0E, 0x00)

time.sleep(0.5)

# LECTURE DES DONNÉES
# -------------------
# Les données d'accélération sont écrites dans le registre 0x00
# La méthode read_i2c_block_data() prend les arguments:
# - l'adresse du module 
# - l'adresse du registre
# - le nombre d'octets à lire

while True:
    data = bus.read_i2c_block_data(0x1D, 0x00, 7)
    
    # Convert the data
    xAccl = (data[1] * 256 + data[2]) / 16
    if xAccl > 2047 :
        xAccl -= 4096

    yAccl = (data[3] * 256 + data[4]) / 16
    if yAccl > 2047 :
        yAccl -= 4096

    zAccl = (data[5] * 256 + data[6]) / 16
    if zAccl > 2047 :
        zAccl -= 4096

    # Affichage
    print("x:",xAccl," y:",yAccl," z:",zAccl)

  