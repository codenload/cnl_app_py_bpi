#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import sdnotify

n = sdnotify.SystemdNotifier()
n.notify("READY=1")

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

while True:
	GPIO.output(21,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(21,GPIO.LOW)
	time.sleep(0.5)
	n.notify("WATCHDOG=1")

