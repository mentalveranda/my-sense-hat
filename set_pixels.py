#!/usr/bin/python
#
# Source: http://pythonhosted.org/sense-hat/api/
#
# File: set_pixels.py
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

sense = SenseHat()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)