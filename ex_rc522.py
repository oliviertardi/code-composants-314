# Préalables
# sudo pip3 install mfrc522-python --break-system-packages
# Et il faut activer le protocole SPI sur le Pi avec la commande "sudo raspi-config"
# 
# Connexions
# Cette composante utilise le protocole SPI, donc les broches 19, 21, 23, 24 et 26
# (notées "SPI0" sur le site https://pinout.xyz/#) du Pi doivent être utilisées.
# SDA:  SPI0 CE0 
# SCK:  SPI0 SCLK
# MOSI: SPI0 MOSI
# MISO: SPI0 MISO
# IRQ:  --
# GND:  GND
# RST:  GPIO 22
# 3.3V: 3.3V
# 
# # Ce programme permet de connecter un senseur RFID RC522 au Pi 
# et à lire les données qu'il envoit

from mfrc522 import SimpleMFRC522


senseur = SimpleMFRC522()

while True:
    print("En attente...")

    identifiant, texte = senseur.read()

    # 3. Print the results
    print("ID: ",identifiant)
    print("Texte: ",texte) 
    print("-----")