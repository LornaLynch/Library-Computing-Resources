# A program to create a burping, flashing jelly baby. 
# Based on the Raspberry Pi Burping Jelly Baby resource (https://www.raspberrypi.org/learning/burping-jelly-baby/) 
# and the Raspberry Pi OCR Flashing LED Recipe card (http://www.ocr.org.uk/Images/125880-recipe-card-flashing-led.pdf).

# Import time and GPIO commands.
import time
import RPi.GPIO as GPIO
import os

# Set the GPIO numbering mode - note that this resource uses the Broadcom numbering system, not the board numbering system.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set pin 3 up as an input so it can receive a signal from your jelly baby "switch".
GPIO.setup(3,GPIO.IN)

# Set pin 27 up as an output so it can power the LED.
GPIO.setup(27,GPIO.OUT)

# Set up a loop which runs forever, and plays the burping sound effect and flashes the LED when the jelly baby is squeezed. 
while True:
    if GPIO.input(3) == False:
        os.system("omxplayer -o local burp.wav")
        time.sleep(1)
        GPIO.output(27,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(27,GPIO.LOW)
        time.sleep(0.2)
        

