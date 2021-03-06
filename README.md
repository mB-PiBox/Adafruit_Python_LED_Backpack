Adafruit Python LED Backpack + individual control over dots in left colon
============================

###:exclamation:Important:exclamation:
Make sure you run `sudo python setup.py install` after replaceing the `SevenSegment.py` to enable individual control over the dots in left colon.

============================

Python library for controlling LED backpack displays such as 8x8 matrices, bar graphs, and 7/14-segment displays on a Raspberry Pi or BeagleBone Black.

Designed specifically to work with the Adafruit LED backpack displays ----> https://learn.adafruit.com/adafruit-led-backpack/overview

For all platforms (Raspberry Pi and Beaglebone Black) make sure your system is able to compile Python extensions.  On Raspbian or Beaglebone Black's Debian/Ubuntu image you can ensure your system is ready by executing:

````
sudo apt-get update
sudo apt-get install build-essential python-dev
````

You will also need to make sure the python-smbus and python-imaging library is installed by executing:

````
sudo apt-get install python-smbus python-imaging
````

Install the library by downloading with the download link on the right, unzipping the archive, navigating inside the library's directory and executing:

````
sudo python setup.py install
````

See example of usage in the examples folder.

###Left Dot Controls
I added the left colon dot control to get a little extra function out of a great 7seg display.
In the clock.py example left colon dot control is used to indicate AM or PM. 
In my personal clock I used it to indication Alarm Set & Snooze Enabled/Disabled.
````
display.set_left_top_dot(True)  #Turn Top Left Dot On
display.set_left_bottom_dot(True)  #Turn Bottom Left Dot On
````



============================
Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!

Written by Tony DiCola for Adafruit Industries.<br>
Modified by mB-PiBox (Marshall)

MIT license, all text above must be included in any redistribution
