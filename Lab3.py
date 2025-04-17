import RPi.GPIO as GPIO
import time

R, G = 26, 19
button = 23
count = -1
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.output(R, GPIO.LOW)
GPIO.output(G, GPIO.LOW)

print("选择任务一或任务二 [1/2]")
state = int(input())

if state == 1:
    print("进入任务一实验环节：")
    GPIO.output(R, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    try:
        while True:
            input_state = GPIO.input(button)
            if not input_state:
                GPIO.output(R, GPIO.HIGH)
                GPIO.output(G, GPIO.LOW)
            elif input_state:
                GPIO.output(R, GPIO.LOW)
                GPIO.output(G, GPIO.HIGH)
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

else:
    print("进入任务二实验环节：")

    def r_on():
        GPIO.output(R, GPIO.HIGH)
        GPIO.output(G, GPIO.LOW)

    def g_on():
        GPIO.output(R, GPIO.LOW)
        GPIO.output(G, GPIO.HIGH)

    def r_twinkle():
        GPIO.output(G, GPIO.LOW)
        GPIO.output(R, GPIO.LOW)
        judge()
        GPIO.output(R, GPIO.HIGH)
        judge()

    def g_twinkle():
        GPIO.output(R, GPIO.LOW)
        GPIO.output(G, GPIO.LOW)
        judge()
        GPIO.output(G, GPIO.HIGH)
        judge()

    def judge():
        global count
        print(count)
        time.sleep(0.1)
        if GPIO.input(button) == GPIO.LOW:
            time.sleep(0.05)
            if GPIO.input(button) == GPIO.LOW:
                count += 1

    try:
        while True:
            if count == -1:
                GPIO.output(R, GPIO.LOW)
                GPIO.output(G, GPIO.LOW)
                judge()
            elif count % 4 == 0:
                r_on()
                judge()
            elif count % 4 == 1:
                while count % 4 == 1:
                    r_twinkle()
            elif count % 4 == 2:
                g_on()
                judge()
            elif count % 4 == 3:
                while count % 4 == 3:
                    g_twinkle()
                    judge()

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
