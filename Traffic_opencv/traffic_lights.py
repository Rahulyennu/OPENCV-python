import RPi.GPIO as GPIO
from subprocess import call
import time
#import subprocess
GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT)#n-r
GPIO.setup(20,GPIO.OUT)#n-y
GPIO.setup(21,GPIO.OUT)#n-g

GPIO.setup(17,GPIO.OUT)#e-r
GPIO.setup(27,GPIO.OUT)#e-y
GPIO.setup(22,GPIO.OUT)#e-g

GPIO.setup(10,GPIO.OUT)#s-r
GPIO.setup(9,GPIO.OUT)#s-y
GPIO.setup(11,GPIO.OUT)#s-g

GPIO.setup(23,GPIO.OUT)#w-r
GPIO.setup(24,GPIO.OUT)#w-y
GPIO.setup(25,GPIO.OUT)#w-g

GPIO.setup(26,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(19,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(6,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


GPIO.setup(2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(3,GPIO.IN ,pull_up_down = GPIO.PUD_UP)
GPIO.setup(4,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(12,GPIO.IN, pull_up_down = GPIO.PUD_UP)
time.sleep(5)
GPIO.add_event_detect(26, GPIO.RISING, callback=lambda x: one(1),bouncetime=200)
GPIO.add_event_detect(19, GPIO.RISING, callback=lambda x: two(1),bouncetime=200)
GPIO.add_event_detect(13, GPIO.RISING, callback=lambda x: three(1),bouncetime=200)
GPIO.add_event_detect(6, GPIO.RISING, callback=lambda x: four(1),bouncetime=200)

x=0
y=0
a=0
b=0

def ambulance():
        
        if(GPIO.input(2) == 1):
                print'AMBULANCE ON NORTH'
                GPIO.output(20,False)
                GPIO.output(27,False)
                GPIO.output(9,False)
                GPIO.output(24,False)

                GPIO.output(21,True)
                GPIO.output(22,False)
                GPIO.output(25,False)
                GPIO.output(11,False)
                
                GPIO.output(16,False)
                GPIO.output(17,True)
                GPIO.output(10,True)
                GPIO.output(23,True)
                while(GPIO.input(2) == 1):
                        pass
                
                
        elif(GPIO.input(3) == 1):
                print'AMBULANCE ON WEST'
                GPIO.output(20,False)
                GPIO.output(27,False)
                GPIO.output(9,False)
                GPIO.output(24,False)

                GPIO.output(21,False)
                GPIO.output(22,False)
                GPIO.output(25,True)
                GPIO.output(11,False)
                
                GPIO.output(16,True)
                GPIO.output(17,True)
                GPIO.output(10,True)
                GPIO.output(23,False)
                while(GPIO.input(3) == 1):
                        pass
        elif(GPIO.input(4) == 1):
                print'AMBULANCE ON EAST'
                GPIO.output(20,False)
                GPIO.output(27,False)
                GPIO.output(9,False)
                GPIO.output(24,False)

                GPIO.output(21,False)
                GPIO.output(22,True)
                GPIO.output(25,False)
                GPIO.output(11,False)
                
                GPIO.output(16,True)
                GPIO.output(17,False)
                GPIO.output(10,True)
                GPIO.output(23,True)
                while(GPIO.input(4) == 1):
                        pass
        elif(GPIO.input(12) == 1):
                print'AMBULANCE ON SOUTH'
                GPIO.output(20,False)
                GPIO.output(27,False)
                GPIO.output(9,False)
                GPIO.output(24,False)

                GPIO.output(21,False)
                GPIO.output(22,False)
                GPIO.output(25,False)
                GPIO.output(11,True)
                
                GPIO.output(16,True)
                GPIO.output(17,True)
                GPIO.output(10,False)
                GPIO.output(23,True)
                while(GPIO.input(12) == 1):
                        pass

def one(ch):
        global y
        ambulance()
        print '!!!!!!!!!!!!!!!!!!!!!!!!!!ONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        x=1
        if(GPIO.input(19) == 1):
            print 'Jam'
        
def two(ch):
        ambulance()
        print '!!!!!!!!!!!!!!!!!!!!!!!!!!two!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        if(GPIO.input(26) == 1):
            print 'Jam'
        
def three(ch):
        ambulance()
        print '!!!!!!!!!!!!!!!!!!!!!!!!!!three!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        if(GPIO.input(13) == 1):
            print 'Jam'
        
def four(ch):
        ambulance()
        print '!!!!!!!!!!!!!!!!!!!!!!!!!!four!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        if(GPIO.input(6) == 1):
            print 'Jam'
        


'''GPIO.add_event_detect(26, GPIO.RISING, callback=one)
GPIO.add_event_detect(19, GPIO.RISING, callback=one)
GPIO.add_event_detect(13, GPIO.RISING, callback=one)
GPIO.add_event_detect(6, GPIO.RISING, callback=one)

GPIO.remove_event_detect(26)
GPIO.remove_event_detect(19)
GPIO.remove_event_detect(13)
GPIO.remove_event_detect(6)'''

def yellow():
        GPIO.output(20,True)
        GPIO.output(27,True)
        GPIO.output(9,True)
        GPIO.output(24,True)

def green():
        GPIO.output(21,True)
        GPIO.output(22,True)
        GPIO.output(25,True)
        GPIO.output(11,True)

def red():
        GPIO.output(16,True)
        GPIO.output(17,True)
        GPIO.output(10,True)
        GPIO.output(23,True)
def clean():
        GPIO.output(20,False)
        GPIO.output(27,False)
        GPIO.output(9,False)
        GPIO.output(24,False)

        GPIO.output(21,False)
        GPIO.output(22,False)
        GPIO.output(25,False)
        GPIO.output(11,False)
        
        GPIO.output(16,False)
        GPIO.output(17,False)
        GPIO.output(10,False)
        GPIO.output(23,False)

def south():
        print'enter south'
        #ambulance()
        GPIO.remove_event_detect(13)
        GPIO.output(20,False)
        GPIO.output(27,False)
        GPIO.output(9,False)
        GPIO.output(24,False)

        GPIO.output(21,False)
        GPIO.output(22,False)
        GPIO.output(25,False)
        GPIO.output(11,True)
        
        GPIO.output(16,True)
        GPIO.output(17,True)
        GPIO.output(10,False)
        GPIO.output(23,True)
        time.sleep(10)
        print'EXITING SOUTH'
        #GPIO.add_event_detect(13, GPIO.RISING, callback=lambda x: three(1),bouncetime=200)
        GPIO.output(9,True)
        time.sleep(2)

def east():
        print'enter east'
        ambulance()
        #GPIO.remove_event_detect(19)
        GPIO.output(20,False)
        GPIO.output(27,False)
        GPIO.output(9,False)
        GPIO.output(24,False)

        GPIO.output(21,False)
        GPIO.output(22,True)
        GPIO.output(25,False)
        GPIO.output(11,False)
        
        GPIO.output(16,True)
        GPIO.output(17,False)
        GPIO.output(10,True)
        GPIO.output(23,True)
        time.sleep(10)
        print'EXITING EAST'
        #GPIO.add_event_detect(19, GPIO.RISING, callback=lambda x: two(1),bouncetime=200)#
        GPIO.output(27,True)
        time.sleep(2)

def west():
        print'enter west'
        ambulance()
        #GPIO.remove_event_detect(6)
        GPIO.output(20,False)
        GPIO.output(27,False)
        GPIO.output(9,False)
        GPIO.output(24,False)

        GPIO.output(21,False)
        GPIO.output(22,False)
        GPIO.output(25,True)
        GPIO.output(11,False)
        
        GPIO.output(16,True)
        GPIO.output(17,True)
        GPIO.output(10,True)
        GPIO.output(23,False)
        time.sleep(10)
        print'EXITING EAST'
        #GPIO.add_event_detect(6, GPIO.RISING, callback=lambda x: four(1),bouncetime=200)
        GPIO.output(24,True)
        time.sleep(2)
        
        
def north():
        print'enter north'
        ambulance()
        #GPIO.remove_event_detect(26)
        GPIO.output(20,False)
        GPIO.output(27,False)
        GPIO.output(9,False)
        GPIO.output(24,False)

        GPIO.output(21,True)
        GPIO.output(22,False)
        GPIO.output(25,False)
        GPIO.output(11,False)
        
        GPIO.output(16,False)
        GPIO.output(17,True)
        GPIO.output(10,True)
        GPIO.output(23,True)
        time.sleep(10)
        print'exiting NORTH'
        #GPIO.add_event_detect(26, GPIO.RISING, callback=lambda x: one(1),bouncetime=200)
        GPIO.output(20,True)
        time.sleep(2)
