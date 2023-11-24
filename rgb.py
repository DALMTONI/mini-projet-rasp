import RPi.GPIO as GPIO
import time

PIN_RED = 17
PIN_GREEN = 27
PIN_BLUE = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)
GPIO.setup(PIN_BLUE, GPIO.OUT)

try:
    while True:
        # Allumer la composante rouge
        GPIO.output(PIN_RED, GPIO.HIGH)
        GPIO.output(PIN_GREEN, GPIO.LOW)
        GPIO.output(PIN_BLUE, GPIO.LOW)
        time.sleep(1)
        # Allumer la composante verte
        GPIO.output(PIN_RED, GPIO.LOW)
        GPIO.output(PIN_GREEN, GPIO.HIGH)
        GPIO.output(PIN_BLUE, GPIO.LOW)
        time.sleep(1)

        # Allumer la composante bleue
        GPIO.output(PIN_RED, GPIO.LOW)
        GPIO.output(PIN_GREEN, GPIO.LOW)
        GPIO.output(PIN_BLUE, GPIO.HIGH)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    
