import RPi.GPIO as GPIO
import time

LED_PINS = [4,27,22]
BUTTON_PIN=23
Trig=24
Echo=25

running=True
start,end=0,0
status=False
count=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PINS, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
GPIO.output(LED_PINS, GPIO.LOW)
GPIO.output(Trig, GPIO.LOW)

def button_callback(channel):
    global running
    running=not running
    print(f"Running state changed to: {'ON' if running else 'OFF'}")

def echo_callback(channel):
    global start
    global end
    global status
    global count

    if GPIO.input(Echo) == GPIO.HIGH or status== False:
        start = time.time()
        status = True

    elif GPIO.input(Echo) == GPIO.LOW and status== True:
        end = time.time()
        duration = end - start
        start, end = 0, 0
        status = False
        global running
        if duration > 0:
            count += 1
            d = duration * 34300 / 2
            print("{:.3f} cm".format(d))
            if count ==10:
                count =0
                running = True

GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(Echo, GPIO.BOTH, callback=echo_callback)

print("Press the button to control the LED flow. Press Ctrl-C to quit.")

try:
    while True:
        if running:
            for pin in LED_PINS:
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(pin, GPIO.LOW)
        else:
            GPIO.output(Trig, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(Trig, GPIO.LOW)
            time.sleep(0.2)
except KeyboardInterrupt:
    print("Keyboard Interrupt")
finally:
    GPIO.cleanup()