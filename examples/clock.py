#!/usr/bin/env python
import os, sys

#	name = "clock.py",
#   version = "0.0.1",
#   author = "mB-PiBox",
#   description = ("A simple clock"),
#   license = "MIT"

import time
import datetime
from Adafruit_LED_Backpack import SevenSegment


# Create display instance on default I2C address (0x70) and bus number.
display = SevenSegment.SevenSegment()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = SevenSegment.SevenSegment(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
display.begin()

#Clear the display
display.clear()

###############################
######## CLOCK CODE ###########
###############################

print "Press CTRL+C to exit"
display.set_brightness(5)

# Continually update the time on a 4 char, 7-segment display
try:
	while(True):
		now = datetime.datetime.now()
		hour = ((now.hour + 11) % 12) + 1
		minute = now.minute
		second = now.second
		ampm = time.strftime("%p")
		# Set Hours
		display.set_digit(0, int(hour / 10))     # Tens
		display.set_digit(1, hour % 10)          # Ones
		# Set Minutes
		display.set_digit(2, int(minute / 10))   # Tens
		display.set_digit(3, minute % 10)        # Ones
		display.set_colon(second % 2)
		if (ampm == "AM"):
			display.set_left_bottom_dot(True)
			display.set_left_top_dot(False)
		else:
			display.set_left_top_dot(True)
			display.set_left_bottom_dot(False)
		display.write_display()
		time.sleep(1)

except KeyboardInterrupt:
	print "\n------------------------------------"
	print "A keyboard interruption was detected"
	print "------------------------------------"

except:
	print "An error or exception has occurred!"

finally:
	print "Cleaning Up"
	time.sleep(1)
	display.clear()
	display.write_display()
