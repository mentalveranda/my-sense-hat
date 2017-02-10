#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)

sense.clear()  # no arguments defaults to off
sleep(1)
sense.clear(red)  # passing in an RGB tuple
sleep(1)
sense.clear(255, 255, 255)  # passing in r, g and b values of a colour

sense.clear()  # no arguments defaults to off

sense.show_message("One small step for Pi!", text_colour=[255, 0, 0])
