import pigpio
import time

# Il y a 3 séquences pour faire tourner le moteur, chacun a ses particularités.
# Il faut en choisir une pour le programme

# Séquence "Single coil" 
seq_simple = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

# Séquence "Full-step" = plus de couple 
seq_full = [
    [1,0,0,1],
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1]
]

# Séquence "Half-step" = plus de précision
seq_half = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]


# GPIO
# M1,...,M4 correspondent aux bobines ("coils") du moteur: attention, ils sont différents des
# numéros INPUT (IN1,...,IN4) de la puce L293D
# Il est important de connecter les bons INPUT sur les bonnes bobines
# Bobine    INPUT
# 1         1
# 2         4
# 3         3
# 4         2
M1,M2,M3,M4 = 21,20,16,12

# Plus la pause est petite, plus le moteur tourne vite. Minimum recommandé: 2ms (0.002)
step_pause = 0.002

def stop_moteur():
    pi.write(M1, 0)
    pi.write(M2, 0)
    pi.write(M3, 0)
    pi.write(M4, 0)

pi = pigpio.pi()

pi.set_mode(M1,pigpio.OUTPUT)
pi.set_mode(M2,pigpio.OUTPUT)
pi.set_mode(M3,pigpio.OUTPUT)
pi.set_mode(M4,pigpio.OUTPUT)

try:
    while True:
        for step in seq_half: # Changez la séquence ici au besoin
            # Activer chacune des 4 bobines
            pi.write(M1, step[0])
            pi.write(M2, step[1])
            pi.write(M3, step[2])
            pi.write(M4, step[3])

            # La durée de la pause détermine la vitesse
            time.sleep(step_pause)

except KeyboardInterrupt:
    stop_moteur()