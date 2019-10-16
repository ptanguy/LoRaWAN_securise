import pycom
from time import sleep

pycom.heartbeat(False)
while True:
    i = 0
    while i < 0xffffff:
        if i < 0x0000ff:
            i += 0x000008
        elif i < 0x00ffff:
            i += 0x000800
        else:
            i += 0x080000
        pycom.rgbled(i)
        print(str(hex(i)))
        sleep(1/60)
