# Détecteur de proximité et de luminosité ambiante
# La luminosité est donnée en lux
# La proximité peut avoir une valeur de 0-1023
# 1023: distance <= 1cm
# 0: distance >= 10cm
# https://www.electronicprojects.net/python/beaglebone-and-tmd2771-proximity-and-ambient-light-sensor-python-example.php

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
# https://www.alldatasheet.com/datasheet-pdf/view/789066/AMSCO/TMD27721.html

# INITIALISATION
# --------------
# Cet appel a pour effet d'activer tout (power ON, Wait ON, ALS ON, proximity ON)
# en mettant les 4 derniers bits du registre à 1
# 0x39 est l'adresse de TMD2771 
# 0x00 est l'adresse du registre où on veut écrire, masquée avec 0xA0
# 0x0F est ce qu'on veut écrire (= les 4 derniers bits à '1')
bus.write_byte_data(0x39, 0x00 | 0xA0, 0x0F)
# Temps de collecte des données de luminosité (ATime)
# 0xDB = 101 ms (cf. p 18)
bus.write_byte_data(0x39, 0x01 | 0xA0, 0xDB)
# Temps de collecte des données de proximité (PTime)
# 0xFF = 2.72 ms (cf. p 19)
bus.write_byte_data(0x39, 0x02 | 0xA0, 0xFF)
# Temps d'attente des données de proximité (WTime)
# 0xFF = 2.72 ms
bus.write_byte_data(0x39, 0x03 | 0xA0, 0xFF)
# Nombre d'impulsions envoyées pour la détection de proximité
# 0x04 = 4
bus.write_byte_data(0x39, 0x0E | 0xA0, 0x04)
# Données diverses (cf. p.23)
bus.write_byte_data(0x39, 0x0F | 0xA0, 0x20)

while True:
    time.sleep(0.5)

    # Lire 6 bytes de données à l'adresse 0x14
    data = bus.read_i2c_block_data(0x39, 0x14 | 0xA0, 6)

    # Conversion des données
    c0_data = data[1] * 256 + data[0]
    c1_data = data[3] * 256 + data[2]
    prox = data[5] * 256 + data[4]
    lumi = 0.0
    CPL = (101.0) / 24.0
    lumi1 = ((1.00 *  c0_data) - (2 * c1_data)) / CPL
    lumi2 = ((0.6 * c0_data) - (1.00 * c1_data)) / CPL
    if lumi1 > 0 and lumi2 > 0 :
        if lumi1 > lumi2 :
            lumi = lumi1
        else :
            lumi = lumi2

    print("Luminosité : ",lumi)
    print("Proximité : ",prox)