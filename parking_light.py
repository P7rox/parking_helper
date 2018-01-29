import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18

GREEN = 17
WHITE = 27
RED = 22

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(WHITE, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

def get_distance():
	GPIO.output(TRIG, GPIO.HIGH)
	time.sleep(0.0001)
	GPIO.output(TRIG, GPIO.LOW)

	while GPIO.input(ECHO) == False :
		start = time.time()

	while  GPIO.input(ECHO) == True :
		end = time.time()

	sig_time = end - start

	#cm
	distance = sig_time / 0.000058 # inches: 0.000148

	print ('Distance: {} cm'.format(distance))
	return distance

def green_light():
	GPIO.output(GREEN, GPIO.HIGH)
	GPIO.output(WHITE, GPIO.LOW)
	GPIO.output(RED, GPIO.LOW)

def white_light():
	GPIO.output(GREEN, GPIO.LOW)
	GPIO.output(WHITE, GPIO.HIGH)
	GPIO.output(RED, GPIO.LOW)

def red_light():
	GPIO.output(GREEN, GPIO.LOW)
	GPIO.output(WHITE, GPIO.LOW)
	GPIO.output(RED, GPIO.HIGH)

try:
	while True:
		distance = get_distance()
		time.sleep(0.05)

		if distance >= 20:
			green_light()
		elif distance >= 10:
			white_light()
		else:
			red_light()

except KeyboardInterrupt:
        #clean up to safe state
        GPIO.cleanup()

