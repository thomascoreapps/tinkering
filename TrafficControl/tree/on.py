
import RPi.GPIO as GPIO
import time

white = 18
blue = 23
topyellow = 24
midyellow = 25
btmyellow = 12
green = 16
red = 20
gate = 21
resetbtn = 6
startbtn = 5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(white,GPIO.OUT) #relay 1 white
GPIO.setup(blue,GPIO.OUT) #relay 2 blue
GPIO.setup(topyellow,GPIO.OUT) #relay 3 yellow1
GPIO.setup(midyellow,GPIO.OUT) #relay 4 yellow2
GPIO.setup(btmyellow,GPIO.OUT) #relay 5 yellow3
GPIO.setup(green,GPIO.OUT) #relay 6 green
GPIO.setup(red,GPIO.OUT) #relay 7 red
GPIO.setup(gate,GPIO.OUT) #relay 8 gate
GPIO.setup(resetbtn,GPIO.IN,pull_up_down=GPIO.PUD_UP) #reset button
GPIO.setup(startbtn,GPIO.IN,pull_up_down=GPIO.PUD_UP) #start button

#all on testing
#while True:
#	GPIO.output(white,GPIO.HIGH) 
#	GPIO.output(blue,GPIO.HIGH) 
#	GPIO.output(topyellow,GPIO.HIGH)
#	GPIO.output(midyellow,GPIO.HIGH)
#	GPIO.output(btmyellow,GPIO.HIGH)
#	GPIO.output(green,GPIO.HIGH)
#	GPIO.output(red,GPIO.HIGH)
#	GPIO.output(gate,GPIO.HIGH)

#all off testing
#	GPIO.output(white,GPIO.LOW)
#	GPIO.output(blue,GPIO.LOW) 
#	GPIO.output(topyellow,GPIO.LOW)
#	GPIO.output(midyellow,GPIO.LOW)
#	GPIO.output(btmyellow,GPIO.LOW)
#	GPIO.output(green,GPIO.LOW)
#	GPIO.output(red,GPIO.LOW)
#	GPIO.output(gate,GPIO.LOW)

while True:
	GPIO.output(red,GPIO.HIGH)
	GPIO.output(white,GPIO.HIGH) 
	GPIO.output(blue,GPIO.HIGH)  
	GPIO.output(topyellow,GPIO.HIGH)
	GPIO.output(midyellow,GPIO.HIGH)
	GPIO.output(btmyellow,GPIO.HIGH)
	GPIO.output(green,GPIO.HIGH)