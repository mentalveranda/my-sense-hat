#!/usr/bin/env python
import time
from sense_hat import SenseHat

sense = SenseHat()

pixels = [
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
]

pixelFrame = pixels
columnIndex = 0
rowIndex = 0
pixelIndex = 0


msleep = lambda x: time.sleep(x / 1000.0)


def next_colour(pix):
    r = pix[0]
    g = pix[1]
    b = pix[2]

    if (r == 255 and g < 255 and b == 0):
        g += 1

    if (g == 255 and r > 0 and b == 0):
        r -= 1

    if (g == 255 and b < 255 and r == 0):
        b += 1

    if (b == 255 and g > 0 and r == 0):
        g -= 1

    if (b == 255 and r < 255 and g == 0):
        r += 1

    if (r == 255 and b > 0 and g == 0):
        b -= 1

    pix[0] = r
    pix[1] = g
    pix[2] = b


while True:
    for pix in pixels:
        next_colour(pix)

    sense.set_pixels(pixels)
    msleep(2)
