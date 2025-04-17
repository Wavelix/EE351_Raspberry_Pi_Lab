import smbus
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
R=23
G=24
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
pwmR=GPIO.PWM(R,70)
pwmR.start(0)
pwmG=GPIO.PWM(G,70)
pwmG.start(0)

bus = smbus.SMBus(1)
address=0x48
control_byte_1 = 0x40
control_byte_2 = 0x41
control_byte_3 = 0x42

def read_analog_input():
    bus.write_byte(address, control_byte_1)
    bus.read_byte(address)
    digital_R = bus.read_byte(address)

    bus.write_byte(address, control_byte_2)
    bus.read_byte(address)
    digital_G = bus.read_byte(address)

    bus.write_byte(address, control_byte_3)
    bus.read_byte(address)
    digital_C = bus.read_byte(address)

    return digital_R, digital_G, digital_C

def convert_to_voltage(digital_R,digital_G):
    ratio_R = digital_R / 255
    ratio_G = digital_G / 255
    light_R = ratio_R * 20
    light_G = ratio_G * 20
    return light_R, light_G

while True:
    digital_R,digital_G,digital_C = read_analog_input()
    print(digital_C)
    if digital_C != 0:
        light_R,light_G=convert_to_voltage(digital_R,digital_G)
        pwmR.ChangeDutyCycle(light_R)
        pwmG.ChangeDutyCycle(light_G)
    else:
        light_R,light_G=convert_to_voltage(digital_R,digital_G)
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        time.sleep(0.2)
        pwmR.ChangeDutyCycle(light_R)
        pwmG.ChangeDutyCycle(light_G)
        time.sleep(0.2)
