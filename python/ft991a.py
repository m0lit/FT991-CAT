#!/usr/bin/env python
import serial
import struct
import time
import datetime
import os
import sys


# Define CAT commands here and frequency varilbles
USB = "MD02;"
FM = "MD04;"
DIG = "MD0C;"
LSB = "MD01;"

usbFreq1 = "144300000"
usbFreq2 = "144330000"
usbFreq3 = "144329900"
BPSKon20 = "014070350"
BPSKon40 = "007035150"
fmFreq1 = "433500000"
fmFreq2 = "433550000"
fmFreq3 = "145500000"
fmFreq4 = "446006250"
CBCH19  = "027781250"


#os.system("sudo amixer cset numid=3 1")
# CAT control of Yaesu FT-897
x=os.system("ls /dev/ttyUSB0")
if x== 0:
	ser = serial.Serial(
  	port='/dev/ttyUSB0',
  	baudrate=9600,
  	parity=serial.PARITY_NONE,
  	stopbits=serial.STOPBITS_ONE,
  	bytesize=serial.EIGHTBITS
	)
else:
	print("no usb availiable")
	time.sleep(2)


# Define getDay procedure to set desired frequency and mode
def setDay():
        myDate = datetime.datetime.today().weekday()
        if (myDate == 0 or myDate == 3):
                CAT(USB)
                setAfreq(usbFreq1)
		setBfreq(usbFreq3)
        elif (myDate == 1):
                CAT(FM)
                setAfreq(fmFreq1)
		setBfreq(fmFreq2)
        else:
                CAT(FM)
                setAfreq(fmFreq3)
        return


# Direct keyboard frequency entry
def setAfreq(myAfreq):
        packAfreq = "FA"+str(myAfreq)+";"
        CAT(packAfreq)
        return

def setBfreq(myBfreq):
	packBfreq = "FB"+str(myBfreq)+";"
	CAT(packBfreq)
	return


# Send CAT commands to Radio by opening the serial port
def CAT(myData):
        if ser.isOpen():
                ser.write(myData)
		myAnswer=ser.read
                ser.close
        return myAnswer


# Turn on/off the Radio
def ON():
	CAT("PS1;")
	time.sleep(1.3)
	CAT("PS1;")
	return

def OFF():
	CAT("PS0;")
	return


# --- MAIN PROGRAM HERE ---
selection=sys.argv[1]

if selection == 'O':
	ON()
	setDay()
elif selection == 'q':
	print ("IT WORKS")
	os.system("sudo touch /home/pi/dev/itworks.txt")
elif selection == '1':
	CAT(USB)
	setAfreq(usbFreq1)
	setBfreq(usbFreq2)
elif selection == '2':
	CAT(USB)
	setAfreq(usbFreq3)
elif selection == '3':
	CAT(FM)
	setAfreq(fmFreq1)
	setBfreq(fmFreq2)
elif selection == '4':
	CAT(FM)
	setAfreq(fmFreq2)
elif selection == '5':
	CAT(DIG)
	setAfreq(BPSKon20)
elif selection == '6':
	CAT(DIG)
	setAfreq(BPSKon40)
elif selection == '7':
	CAT(FM)
	setAfreq(CBCH19)
elif selection == '8':
	CAT(FM)
	setAfreq(fmFreq4)
elif selection == 'T':
	CAT("TX1;")
elif selection == 'F':
	OFF()
elif selection == 'R':
	CAT("TX0;")
elif selection == 'C':
	#CAT("TX1;")
	mystring="espeak -p 100 "+"golf xray four whiskey bravo charlie this is M 0 L I T calling and listening"
	os.system(mystring)
	time.sleep(1)
	#CAT("TX0;")
