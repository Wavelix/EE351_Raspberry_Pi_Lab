import smbus
import time

address=0x48
controlbit=0x42
bus=smbus.SMBus(1)
while True:
    bus.write_byte(address, controlbit)
    a = bus.read_byte(address)
    for i in range(130,210,1):
        bus.write_byte_data(address, controlbit, i)
        time.sleep(0.01)
    for i in range(210,130,-1):
        bus.write_byte_data(address, controlbit, i)
        time.sleep(0.01)
