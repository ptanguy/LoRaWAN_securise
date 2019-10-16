import pycom
from time import sleep
pycom.heartbeat(False)
pycom.rgbled(0x8f0080)
sleep(2)