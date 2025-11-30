import pigpio

CLK = 21   
DAT = 20    

pi = pigpio.pi()
pi.set_mode(CLK, pigpio.INPUT)
pi.set_mode(DAT, pigpio.INPUT)
pi.set_pull_up_down(CLK, pigpio.PUD_UP)
pi.set_pull_up_down(DAT, pigpio.PUD_UP)

dernier = pi.read(CLK)

# Le fonctionnement du rotary encoder:
# La rotation de la tige se fait par incrémentation (on le sent lorsqu'on la tourne)
# À chaque incrémentation de la rotation, la valeur de CLK change. Lors de ce changement,
# c'est la valeur de DAT qui nous indique le sens de rotation. 
# Si CLK et DAT sont différents, la rotation est horaire; si les valeurs sont identiques,
# Explication visuelle: https://www.youtube.com/watch?v=v4BbSzJ-hz4
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

