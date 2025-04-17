import RPi.GPIO as GPIO
import time
R,G,B=26,19,13
GPIO.setmode(GPIO.BCM)

GPIO.setup(R,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.output(R,GPIO.LOW)
GPIO.output(G,GPIO.LOW)
GPIO.output(B,GPIO.LOW)

t=0.5
try:
    while True:
        GPIO.output(R,GPIO.HIGH)
        GPIO.output(G,GPIO.LOW)
        GPIO.output(B,GPIO.LOW)
        time.sleep(t)
        GPIO.output(R,GPIO.LOW)
        GPIO.output(G,GPIO.HIGH)
        GPIO.output(B,GPIO.LOW)
        time.sleep(t)
        GPIO.output(R,GPIO.LOW)
        GPIO.output(G,GPIO.LOW)
        GPIO.output(B,GPIO.HIGH)
        time.sleep(t)
except KeyboardInterrupt:
    print("程序中断")

finally:
    GPIO.cleanup()