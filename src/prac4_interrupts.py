# A class which contains functions that fire on interrupts. Tries to return the
# return of the contained function up the chain as effectively as possible.

import RPi.GPIO as GPIO

class interruptHandler:

    button1 = 0
    button2 = 0
    button3 = 0
    button4 = 0
    bounce = 400

    def __init__(self, b1, f1, b2, f2, b3, f3, b4, f4):

        """
        Initializer which sets buttons tied to gpio pins and connects them to functions
        """
        GPIO.setmode(GPIO.BCM)
        
        # Store set button pins
        self.button1 = b1
        self.button2 = b2
        self.button3 = b3
        self.button4 = b4

        GPIO.setup(self.button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(self.button1, GPIO.RISING, callback=f1, bouncetime=self.bounce)
        GPIO.add_event_detect(self.button2, GPIO.RISING, callback=f2, bouncetime=self.bounce)
        GPIO.add_event_detect(self.button3, GPIO.RISING, callback=f3, bouncetime=self.bounce)
        GPIO.add_event_detect(self.button4, GPIO.RISING, callback=f4, bouncetime=self.bounce)

