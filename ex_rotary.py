import pigpio

CLK = 21   # Pin for CLK signal
DAT = 20    # Pin for DAT signal

pi = pigpio.pi()
pi.set_mode(CLK, pigpio.INPUT)
pi.set_mode(DAT, pigpio.INPUT)
pi.set_pull_up_down(CLK, pigpio.PUD_UP)
pi.set_pull_up_down(DAT, pigpio.PUD_UP)

dernier = pi.read(CLK)

# Le fonctionnement du rotary encoder:
# La rotation de la tige se fait par incrémentation (on le sent lorsqu'on la tourne)
# À chaque incrémentation de la rotation, deux contacts électriques (sur CLK et DAT) se produisent. 
# Si CLK et DAT sont différents
try:
    while True:
        etat = pi.read(CLK)
        if etat != dernier:
            lecture_DAT = pi.read(DAT)
            if lecture_DAT != etat:
                direction = "Horaire"
            else:
                direction = "Antihoraire"
            print(direction)
        dernier = etat

except KeyboardInterrupt:
    pi.stop()
    print("Terminé.")

