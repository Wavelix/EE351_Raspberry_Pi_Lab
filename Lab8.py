import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
io = 17
GPIO.setup(io, GPIO.OUT)
pwm = GPIO.PWM(io, 440)

notes = {
    'C4': 261,
    'D4': 294,
    'E4': 329,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 493,
    'C5': 523
}

def play(W, duration, volume=10):
    pwm.ChangeFrequency(W)
    pwm.start(volume)
    time.sleep(duration)
    pwm.stop()

song = [
    ('E4', 0.4), ('E4', 0.4), ('F4', 0.4), ('G4', 0.4),
    ('G4', 0.4), ('F4', 0.4), ('E4', 0.4), ('D4', 0.4),
    ('C4', 0.4), ('C4', 0.4), ('D4', 0.4), ('E4', 0.4),
    ('E4', 0.6), ('D4', 0.2), ('D4', 0.8),
]

try:
    for note, duration in song:
        play(notes[note], duration, volume=20)
        time.sleep(0.05)
finally:
    GPIO.cleanup()
