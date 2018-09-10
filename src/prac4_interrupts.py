# A class which contains functions that fire on interrupts. Tries to return the
# return of the contained function up the chain as effectively as possible.

import RPi.GPIO as GPIO

class interruptHandler:

    button1 = 0
    button2 = 0
    button3 = 0

    def __init__(self, b1, b2, b3):
        """
        Initializer which sets buttons tied to gpio pins and connects them to functions
        """
        GPIO.setmode(GPIO.BCM)
        
        # Store set button pins
        self.button1 = b1
        self.button2 = b2
        self.button3 = b3

        GPIO.setup(self.button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(self.button1, GPIO.FALLING, callback=b1callback, bouncetime=200)
        GPIO.add_event_detect(self.button2, GPIO.FALLING, callback=b2callback, bouncetime=200)
        GPIO.add_event_detect(self.button3, GPIO.FALLING, callback=b3callback, bouncetime=200)

    def b1callback(f):
        return f

    def b2callback(f):
        return f

    def b3callback(f):
        return f


