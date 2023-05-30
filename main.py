from microbit import *
import time

#fonction pour l'avancement 
def robotAvance(vitesse):
    pin1.write_analog(vitesse)
    pin2.write_analog(vitesse)
    pin8.write_digital(0)
    pin12.write_digital(0)
    
# fonction pour le pivotement 
def robotPivote(vitesse,sens):
   
    pin1.write_analog(vitesse)
    pin2.write_analog(vitesse)
    pin8.write_digital(1-sens)
    pin12.write_digital(sens)
#fonction pour l'arret 
def robotStoppe():
    pin1.write_analog(0)
    pin2.write_analog(0)
 #fonction pour mesurer la distance en utilisant le capteur ultrason  
def MesureDistance():
    pin13.write_digital(1)
    time.sleep_us(10)
    pin13.write_digital(0)
    
    echo=pin14.read_digital()
    while (echo ==0):
        echo = pin14.read_digital()
    t0 =time.ticks_us()
      
    while (echo ==1):
        echo = pin14.read_digital()
    t1 = time.ticks_us()
      
    d= (t1-t0)//58
    return(d)

display.off()

while True:
    d_cm=MesureDistance()
    if d_cm>20:
        robotAvance(150)
    else :
        robotPivote(150,1)
