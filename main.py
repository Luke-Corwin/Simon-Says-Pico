from machine import Pin
from time import sleep
import random

leds = [
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT),
    Pin(5, Pin.OUT)
    ]

buttons = [
    Pin(10, Pin.IN, Pin.PULL_UP), #red
    Pin(11, Pin.IN, Pin.PULL_UP), #blue
    Pin(12, Pin.IN, Pin.PULL_UP), #yellow
    Pin(13, Pin.IN, Pin.PULL_UP) #white
    ]

buzzer = Pin(15, Pin.OUT)

def beep(length):
    buzzer.on()
    sleep(length)
    buzzer.off()
    
def flash(index):
    leds[index].on()
    
    beep(0.05)
    
    sleep(0.2)
    
    leds[index].off()
    
    sleep(0.2)
    
    

def get_press():
    while True:
        
        for i in range(4):
            if buttons[i].value() == 0:
                
                leds[i].on()
                
                beep(0.05)
                
                sleep(0.2)
                
                leds[i].off()
                
                while buttons[i].value() == 0:
                    
                    sleep(0.01)
                
                return i 
def lose():
    for i in range(3):
        
        for led in leds:
            led.on()
        
        buzzer.on()
        
        sleep(0.3)
        
        for led in leds:
            led.off()
            
        buzzer.off()
        
        sleep(0.3)
        
for i in range(4):
    
    leds[i].on()
    beep(0.05)
    sleep(0.15)
    leds[i].off()
    
sleep(1)

sequence = []

while True:
    sequence.append(
        random.randint(0, 3)   
    )
    
    sleep(0.5)

    for i in sequence:
        flash(i)
    sleep(1)
    correct = True
    
    for i in sequence:
        player = get_press()
        
        if player != i:
            correct = False
            break
    if not correct:
        lose()
        
        print("Game Over")
        print("Score:", len(sequence) -1)
        
        break
    
    print("Correct Sequence")
    print("Score:", len(sequence))
    
    sleep(1)