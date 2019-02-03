import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

count = 1
print('Print number of times to repeat: ',end="")
repeatcount = int(input())

print('How many seconds should it stay lit: ', end='')
staylit = float(input())

while count <= repeatcount:
	GPIO.output(18,GPIO.HIGH)
	time.sleep(staylit)

	GPIO.output(18,GPIO.LOW)
	time.sleep(staylit)

	count += 1
