#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import Adafruit_MCP3008
import os
from time import localtime, strftime

GPIO.setmode(GPIO.BCM)

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
output = [0]*5     #create array of 5 fields to display time,timer,pot,temp,light
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
#Return voltage reading on pot
def getPot():
    adcPot = values[1];
    vPot = (float(adcPot)*5)/1024
    return vPot;

#get CH2
#CH2 = Temp: MCP9700A. 1.5v @ 100C -> y = 100(T)
#Vout = (Tcoef)(Tamb)+V0 :Tcoef=10.0mV/C, V0=500mV
#Temperature = (Vout -V0)*(5/1024)/Tcoef
def getTemp():
    adcOut = values[2]
    vOut = (float(adcOut)*5)/1024
    temp = (vOut-0.5)/0.01
    return temp;

def formatOutput():
    #Insert sys time here
    output[0] = strftime("%H:%M:%S", localtime())
    #Insert interrupt time here
    output[1] = " Timer\t"
    output[2] = str(round(getPot(),2)) +  " V\t "
    output[3] = str(round(getTemp(),2)) + " C\t "
    output[4] = str(round(getLight(),2)) +"%\t "

while True:
    updateADCVals();
    #load adc vals into output array
    formatOutput();
    # delay for 100ms
    time.sleep(0.1)
    #print output with lines between values
    print ' | '.join(output)


