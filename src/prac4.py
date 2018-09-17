import prac4_SPI
import prac4_interrupts
import time
import sys

frequency = 0 # currently selected frequency

flist = [0.5,1,2] # possible frequencies

started = True # are sensors running

timer = 0 # Time since last reset

values = prac4_SPI.values

output = prac4_SPI.output

def reset(port):
    global timer = 0
    sys.stdout.write("\u001b[2J")
    print("reset timer")


def freq(port):
    global frequency = ((frequency + 1) % 3)
    print("New frequency: " + str(flist[frequency]))

def stop(port):
    global started = not started
    print("Set Sensors Running: " + str(started))

def disp(port):
    print("pressed display"+str(port))

handler = prac4_interrupts.interruptHandler(2, reset, 3, freq, 4, stop, 14, disp)

while True:
    time.sleep(flist[frequency])
    
    if started:
        prac4_SPI.updateADCVals()
        prac4_SPI.formatOutput()
        
        print( ' | '.join(output))


