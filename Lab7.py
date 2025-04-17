import RPi.GPIO as GPIO
import time

Trig=17
Echo=18
R=22

GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(R, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

GPIO.output(Trig, GPIO.LOW)
GPIO.output(R, GPIO.LOW)

def warning(d):
    if d<5:
        GPIO.output(R, GPIO.HIGH)
    elif d<10:
        GPIO.output(R, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(R, GPIO.LOW)
    elif d<30:
        GPIO.output(R, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(R, GPIO.LOW)
    else:
        GPIO.output(R, GPIO.LOW)

try:
    while True:
        GPIO.output(Trig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(Trig, GPIO.LOW)
        while True:
            if GPIO.input(Echo) == GPIO.LOW:
                continue
            else:
                break
        start = time.time()
        while True:
            if GPIO.input(Echo) == GPIO.HIGH:
                continue
            else:
                break
        end = time.time()
        d = (end - start) * 343*100 / 2
        warning(d)
        print("{:.3f} cm".format(d))
        time.sleep(0.2)


except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
