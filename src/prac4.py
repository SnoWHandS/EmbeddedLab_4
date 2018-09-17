import prac4_SPI
import prac4_interrupts

def reset():
    print("pressed reset")

def freq():
    print("pressed frequency")

def stop():
    print("pressed stop")

def disp():
    print("pressed display")

handler = prac4_interrupts.interruptHandler(self, 2, reset(), 3, freq(), 4, stop(), 14, disp())


