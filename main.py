#!/usr/bin/env python3
"""
__authors__    = ["Blaze Sanders", "Vladyslav Haverdovskyi"]
__contact__    = "blazes@mfc.us"
__copyright__  = "Copyright 2023"
__license__    = "MIT License"
__status__     = "Development"
__deprecated__ = False
__version__    = "0.0.1"
__doc__        = "Terminal app running on a NVIDIA Jetson Nano to control a table for flipping 2000 lbs house walls (panels)"
"""

## Standard library
# Allow program to extract filename of the current file
import sys, os.path
v2024_0 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(v2024_0)

# Allow program to pause operation and create local timestamps
from builtins import ImportError, len, NameError
from time import sleep


## 3rd party libraries
# Allow control of output devices such as Motors, Servos, LEDs, and Relays
# https://gpiozero.readthedocs.io/en/stable/installing.html
from gpiozero import Motor, Servo, LED, Energenie, OutputDevice, AngularServo

# Allow control of input devices such as Buttons
from gpiozero import Button

# Check status of network / new device IP addresses and Pi hardware
from gpiozero import PingServer, pi_info

# Useful pin status tools and math tools
from gpiozero.tools import all_values, negated, sin_values

# Useful for controlling devices based on date and time
from gpiozero import TimeOfDay

# Allow 'dependency-free' playback of .wav audio on Linux, MacOS, & Windows
# https://simpleaudio.readthedocs.io/en/latest/
import simpleaudio as sa


if __name__ == "__main__":
	print("https://github.com/ROBO-BEV/Tapomatic/blob/master/v2020.0/Actuator/Actuator.py")
	print("https://samplefocus.com/categories/noise?min_tempo=0&max_tempo=200&sort_by=Popular")
	print("https://pixabay.com/sound-effects/search/reload/")
