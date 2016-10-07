from time import sleep
import pifacedigitalio as p

DELAY = 10.0
laps = 0
p.init()
while(True):
    p.digital_read(0)
    if (p.digital_read(0) == 1) :
        print ("output on")
        p.digital_write(0,1)
        sleep(DELAY)
        p.digital_write(0,0)
    
    
    
    
    else :
            print ("output off")
        
            
