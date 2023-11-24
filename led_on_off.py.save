#!/usr/bin/python
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

etat= int(sys.argv[1])

if etat == 1:

        GPIO.output(4, GPIO.HIGH)

elif etat == 0:

        GPIO.output(4, GPIO.LOW)






