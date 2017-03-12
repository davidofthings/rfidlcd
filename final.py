#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import buzzer
import Adafruit_CharLCD as LCD

GPIO.setmode(GPIO.BCM)

# Setting BCM parameters
lcd_rs = 26
lcd_en = 24
lcd_d4 = 13
lcd_d5 = 6
lcd_d6 = 5
lcd_d7 = 12
lcd_backlight = 4

# Column and row size
lcd_columns = 16
lcd_rows =2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "\nCtrl+C captured, clearing screen and ending read."
    lcd.clear()
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Test, Welcome"
lcd.message('Test, Welcome -\nReady to Scan')

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected."
        lcd.clear()
	lcd.message('ID: ' +str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]) + '\nPan Scanned!')
	
        # Print UID
        print "ID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
        
	# Buzz, Light!
        GPIO.output(23, GPIO.HIGH)
        time.sleep(.3)
        GPIO.output(23, GPIO.LOW)
        time.sleep(4)
        lcd.clear()

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            print 'Success!'
        
        else:
            lcd.message('Error! Please Rescan\nThe Card!')
            print 'Authentication Error!'
            time.sleep(4)
            lcd.clear()


    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

   
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        lcd.message('Test, Welcome -\nReady to Scan')
        continue_reading = True

        #print "Ready to scan another pan."
