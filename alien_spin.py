#!/usr/bin/python
#
# Source: http://pythonhosted.org/sense-hat/api/
#
# File: alien_spin.py
#
# Description: 
#   Updates the entire LED matrix based on a 64 length list of pixel values.
#
# Parameters:
#   pixel_list - [List], [[R, G, B] * 64]
#   A list containing 64 smaller lists of [R, G, B] pixels (red, green, blue). Each R-G-B element must be an integer between 0 and 255.
#
# Returns: 
#   None
#

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White
o = [0, 0, 0]   #Off

alien_one = [
O, O, O, X, X, O, O, O,
O, O, X, X, X, X, O, O,
O, X, X, X, X, X, X, O,
X, X, O, X, X, O, X, X,
X, X, X, X, X, X, X, X,
O, O, X, O, O, X, O, O,
O, X, O, X, X, O, X, O,
X, O, X, O, O, X, O, X
]

alien_two = [
o, o, o, X, X, o, o, o,
o, o, X, X, X, X, o, o,
o, X, X, X, X, X, X, o,
X, X, o, X, X, o, X, X,
X, X, X, X, X, X, X, X,
o, o, X, o, o, X, o, o,
o, X, o, X, X, o, X, o,
X, o, X, o, o, X, o, X
]

sense.clear()  # no arguments defaults to off

sense.set_pixels(alien_one)
sleep(1)

sense.set_pixels(alien_two)
sleep(1)
sense.set_pixels(alien_one)
sleep(1)

sense.set_pixels(alien_two)
sleep(1)
sense.set_pixels(alien_one)
sleep(1)

sense.set_pixels(alien_two)
sleep(1)
sense.set_pixels(alien_one)
sleep(1)

sense.set_pixels(alien_two)
sleep(1)
sense.set_pixels(alien_one)
sleep(1)

sense.set_pixels(alien_two)
sleep(1)
sense.clear()  # no arguments defaults to off

