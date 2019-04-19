import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
trig = 40
echo = 38
led1 = 29
led2 = 31
led3 = 33
led4 = 35
led5 = 37
#led6 = 3
#led7 = 5
#led8 = 7
#led9 = 11

gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)
gpio.setup(led1,gpio.OUT)
gpio.setup(led2,gpio.OUT)
gpio.setup(led3,gpio.OUT)
gpio.setup(led4,gpio.OUT)
gpio.setup(led5,gpio.OUT)
#gpio.setup(led6,gpio.OUT)
#gpio.setup(led7,gpio.OUT)
#gpio.setup(led8,gpio.OUT)
#gpio.setup(led9,gpio.OUT)

while True:
    gpio.output(trig,False)
    time.sleep(.05)
    gpio.output(trig,True)
    time.sleep(.05)
    gpio.output(trig,False)

    while(gpio.input(echo) == 0):
        start = time.time()
    while(gpio.input(echo) == 1):
        end = time.time()
    length = end - start
    distance = length * 17150
    distance = round(distance, 2)
    print "Distance: ", distance, " cm"

    if(distance > 140):
        gpio.output(led1,False)
        gpio.output(led2,False)
        gpio.output(led3,False)
        gpio.output(led4,False)
        gpio.output(led5,False)
        #gpio.output(led6,False)
        #gpio.output(led7,False)
        #gpio.output(led8,False)
        #gpio.output(led9,False)
    if(distance < 140 and distance > 110):
        gpio.output(led1,True)
        gpio.output(led2,False)
        gpio.output(led3,False)
        gpio.output(led4,False)
        gpio.output(led5,False)
        #gpio.output(led6,False)
        #gpio.output(led7,False)
        #gpio.output(led8,False)
        #gpio.output(led9,False)        
    if(distance < 110 and distance > 80):
        gpio.output(led1,True)
        gpio.output(led2,True)
        gpio.output(led3,False)
        gpio.output(led4,False)
        gpio.output(led5,False)
        #gpio.output(led6,False)
        #gpio.output(led7,False)
        #gpio.output(led8,False)
        #gpio.output(led9,False)
    if(distance < 80 and distance > 50):
        gpio.output(led1,True)
        gpio.output(led2,True)
        gpio.output(led3,True)
        gpio.output(led4,False)
        gpio.output(led5,False)
        #gpio.output(led6,False)
        #gpio.output(led7,False)
        #gpio.output(led8,False)
        #gpio.output(led9,False)
    if(distance < 50 and distance > 20):
        gpio.output(led1,True)
        gpio.output(led2,True)
        gpio.output(led3,True)
        gpio.output(led4,True)
        gpio.output(led5,False)
        #gpio.output(led6,False)
        #gpio.output(led7,False)
        #gpio.output(led8,False)
        #gpio.output(led9,False)
    if(distance < 20):
        gpio.output(led1,True)
        gpio.output(led2,True)
        gpio.output(led3,True)
        gpio.output(led4,True)
        gpio.output(led5,True)
        #gpio.output(led6,False)
        #gpio.output(led7,False)
        #gpio.output(led8,False)
        #gpio.output(led9,False)
        


