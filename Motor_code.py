import RPi.GPIO as GPIO

from time import sleep

ENA = 17
#0-255 speed
IN1 = 27

IN2 = 22
#one on and one off for direction

ENB = 10
IN3 = 11
IN4 = 9

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

def forwardA(x):
    GPIO.output(ENA,x)
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    
def backwardA(x):
    GPIO.output(ENA,x)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
def forwardB(x):
    GPIO.output(ENB,x)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
def backwardB(x):
    GPIO.output(ENB,x)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
def stop():
    GPIO.output(ENA,0)
    GPIO.output(ENB,0)
for z in range (52):
    forwardA(200)
    sleep(0.5)
    backwardA(200)
    sleep(0.5)
    stop()



    