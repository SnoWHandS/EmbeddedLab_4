import prac4_SPI
import prac4_interrupts
import time

def reset(port):
    print("pressed reset"+str(port))

def freq(port):
    print("pressed frequency"+str(port))

def stop(port):
    print("pressed stop"+str(port))

def disp(port):
    print("pressed display"+str(port))

handler = prac4_interrupts.interruptHandler(self, 2, reset(), 3, freq(), 4, stop(), 14, disp())

while True:
    time.sleep(0)
