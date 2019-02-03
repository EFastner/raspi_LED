import RPi.GPIO as GPIO
import time

#Set Raspberry Pi to BCM Mode
GPIO.setmode(GPIO.BCM)

#Define the pin numbers for each LED and add to a list
red_pin = 16
blue_pin = 21
green_pin = 20
chan_list = [red_pin, blue_pin, green_pin]

#Setup pins defined above
GPIO.setup(chan_list, GPIO.OUT)

#Set a PWM for each pin so that we can control the brightness
RED_LED = GPIO.PWM(red_pin, 100)
BLUE_LED = GPIO.PWM(blue_pin, 100)
GREEN_LED = GPIO.PWM(green_pin, 100)

RED_LED.start(75)
time.sleep(5)

GREEN_LED.start(75)
time.sleep(5)

BLUE_LED.start(75)
time.sleep(5)

RED_LED.stop()
GREEN_LED.stop()
BLUE_LED.stop()

GPIO.cleanup()
