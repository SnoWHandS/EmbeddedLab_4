import prac4_SPI
import prac4_interrupts
import collections
import time
import datetime
import sys

frequency = 0 # currently selected frequency

flist = [0.5,1,2] # possible frequencies

started = True # are sensors running

starttime = time.time() # Time since last reset

values = prac4_SPI.values

output = prac4_SPI.output

readqueue =  collections.deque()

readqueue.maxlen = 5

def reset(port):
    global timer
    timer = time.time()
    sys.stdout.write("\u001b[2J")
    print("reset timer")


def freq(port):
    global frequency
    frequency = ((frequency + 1) % 3)
    print("New frequency: " + str(flist[frequency]))


def stop(port):
    global started
    started = not started
    print("Set Sensors Running: " + str(started))


def disp(port):
    print("pressed display"+str(port))
    global readqueue

    for k in readqueue:
        print(k)

handler = prac4_interrupts.interruptHandler(2, reset, 3, freq, 4, stop, 14, disp)

while True:
    time.sleep(flist[frequency])

    readqueue.clear()
    prac4_SPI.updateADCVals()
    prac4_SPI.formatOutput()
    localtime = time.localtime()
    output[1] = datetime.datetime.fromtimestamp(localtime-starttime).strftime("%H:%M:%S")
    output[0] = datetime.datetime.fromtimestamp(localtime).strftime('%H:%M:%S')
    outstring = ' | '.join(output)

    if started:
        readqueue.clear()
        print(outstring)
    else:
        readqueue.append(outstring)


