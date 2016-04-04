# A program to help children create a cardboard model robot with a flashing antenna.
# Based on the Raspberry Pi Robot Antenna learning resource available at https://www.raspberrypi.org/learning/robot-antenna/


# Make your robot's antenna flash on and off a number of times. 

# Import time and GPIO commands
import time
import RPi.GPIO as GPIO

# Set the GPIO numbering mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Set pin 17 up as an output so it can power the LED
GPIO.setup(17,GPIO.OUT)

# Set the LED to flash on and off five times  
for x in range (0,5):
  print("Beep!")
  GPIO.output(17,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(17,GPIO.LOW)
  time.sleep(1)
  
# If you want the LED to flash repeatedly, replace the line of code setting the number of flashes
# for x in range (0,5):
# with the line below
# while True:  
# The LED will now continue to flash; press Ctrl + C to quit 
