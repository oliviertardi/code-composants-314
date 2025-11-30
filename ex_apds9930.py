import time
import smbus2

# Constantes
I2C_ADDR = 0x39
REG_ENABLE = 0x00
REG_CTRL = 0x0f
REG_ATIME = 0x01
REG_WTIME = 0x03
REG_PROXPULSE = 0x0E
REG_PROXOFFSET = 0x1E
REG_CONFIG = 0x0D
REG_PERS = 0x0C
GAIN_LUM = 2
PILT = 0
PIHT = 50
AILT = 65535
AIHT = 0
PDRIVE,PDIODE,PGAIN,AGAIN = 0,2,3,2

bus = smbus2.SMBus(1)

bus.write_byte_data(I2C_ADDR, REG_ENABLE, 0x00)
bus.write_byte_data(I2C_ADDR, REG_ATIME, 0xff)
bus.write_byte_data(I2C_ADDR, REG_WTIME, 0xff)
bus.write_byte_data(I2C_ADDR, REG_PROXPULSE, 0x08)
bus.write_byte_data(I2C_ADDR, REG_PROXOFFSET, 0x00)
bus.write_byte_data(I2C_ADDR, REG_CONFIG, 0x00)
bus.write_byte_data(I2C_ADDR, REG_PERS, 0x22)
bus.write_byte_data(I2C_ADDR, REG_CTRL, PDRIVE | PDIODE | PGAIN | AGAIN)
bus.write_byte_data(I2C_ADDR, 0x08, 0x0f)

h = PILT >> 8
l = PILT & 0x00FF
bus.write_byte_data(I2C_ADDR, 0x08, l)
bus.write_byte_data(I2C_ADDR, 0x09, h)

h = PIHT >> 8
l = PIHT & 0x00FF
bus.write_byte_data(I2C_ADDR, 0x0A, l)
bus.write_byte_data(I2C_ADDR, 0x0B, h)

h = AILT >> 8
l = AILT & 0x00FF
bus.write_byte_data(I2C_ADDR, 0x04, l)
bus.write_byte_data(I2C_ADDR, 0x05, h)

h = AIHT >> 8
l = AIHT & 0x00FF
bus.write_byte_data(I2C_ADDR, 0x06, l)
bus.write_byte_data(I2C_ADDR, 0x07, h)

bus.write_byte_data(I2C_ADDR, REG_ENABLE, 0x0f)

try:
    while True:
        
        time.sleep(0.5)
        # Luminosité canal 0
        l = bus.read_byte_data(I2C_ADDR, 0x14)
        h = bus.read_byte_data(I2C_ADDR, 0x15)
        lum0 = l + (h << 8)
        
        # Luminosité canal 0
        l = bus.read_byte_data(I2C_ADDR, 0x16)
        h = bus.read_byte_data(I2C_ADDR, 0x17)
        lum1 = l + (h << 8)

        # Luminosité ambiante
        iac = max(lum0 - 1.862 * lum1, 0.746 * lum0 - 1.291 * lum1)
        lpc = 0.49 * 52 / (2.73 * GAIN_LUM)
        lum =  iac * lpc
    
        # Proximité
        l = bus.read_byte_data(I2C_ADDR, 0x18)
        h = bus.read_byte_data(I2C_ADDR, 0x19)
        prox = l + (h << 8)
    
        print(lum0,lum1,lum,prox)
        a = bus.read_byte_data(I2C_ADDR, 0x14)
        b = bus.read_byte_data(I2C_ADDR, 0x16)
        c = bus.read_byte_data(I2C_ADDR, 0x18)
        #print(a,b,c)

except KeyboardInterrupt:
    print("Terminé.")


