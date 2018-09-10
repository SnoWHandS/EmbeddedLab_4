#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import Adafruit_MCP3008
import os

GPIO.setmode(GPIO.BCM)

# Open SPI bus
#spi = spidev.SpiDev()
# create spi object
#spi.open(0,0)

# pin definition
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)


mcp = Adafruit_MCP3008.MCP3008(clk=SPICLK,
        cs=SPICS,
        mosi=SPIMOSI, 
        miso=SPIMISO)
# global variable
values = [0]*4

#--------------gets a SPI data--------------
#update channel values array
def updateADCVals():
    for i in range(4):
        values[i] = mcp.read_adc(i)
    return;

#get CH0
#CH0 = LDR with 6.9K above --\/\/--Ch0--LDR--Gnd
#ADC Bounds between 0 - 800
def getLight():
    adcLgt = values[0];
    light = ((800 - float(adcLgt))/800)*100
    return light;

#get CH1
def getPot():
    return values[1];

#get CH2
#CH2 = Temp: MCP9700A. 1.5v @ 100C -> y = 100(T)
#Vout = (Tcoef)(Tamb)+V0 :Tcoef=10.0mV/C, V0=500mV
#Temperature = (Vout-V0)*(5/1024)/Tcoef
def getTemp():
    adcOut = values[2]
    vOut = (float(adcOut*5))/1024
    temp = (vOut-0.5)/0.01
    return temp;

while True:
    updateADCVals();
    # delay for a half second
    time.sleep(0.001)
    print "temperature is:"
    print getTemp()
    print "Light is:"
    print getLight()


