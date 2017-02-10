#!/usr/bin/env python
import time
from sense_hat import SenseHat
from time import sleep


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

pixelsTwo = [
    [255, 0, 0], [255, 0, 0], [255, 87, 0], [255, 196, 0], [205, 255, 0], [95, 255, 0], [0, 255, 13], [0, 255, 122],
    [255, 0, 0], [255, 96, 0], [255, 205, 0], [196, 255, 0], [87, 255, 0], [0, 255, 22], [0, 255, 131], [0, 255, 240],
    [255, 105, 0], [255, 214, 0], [187, 255, 0], [78, 255, 0], [0, 255, 30], [0, 255, 140], [0, 255, 248], [0, 152, 255],
    [255, 223, 0], [178, 255, 0], [70, 255, 0], [0, 255, 40], [0, 255, 148], [0, 253, 255], [0, 144, 255], [0, 34, 255],
    [170, 255, 0], [61, 255, 0], [0, 255, 48], [0, 255, 157], [0, 243, 255], [0, 134, 255], [0, 26, 255], [83, 0, 255],
    [52, 255, 0], [0, 255, 57], [0, 255, 166], [0, 235, 255], [0, 126, 255], [0, 17, 255], [92, 0, 255], [201, 0, 255],
    [0, 255, 66], [0, 255, 174], [0, 226, 255], [0, 117, 255], [0, 8, 255], [100, 0, 255], [210, 0, 255], [255, 0, 192],
    [0, 255, 183], [0, 217, 255], [0, 109, 255], [0, 0, 255], [110, 0, 255], [218, 0, 255], [255, 0, 183], [255, 0, 74]
]

pixelFrame = pixels

pixelMax = 63
pixleFirst = 0

columnIndex = 0
rowIndex = 0
pixelIndex = 0
columnMax = 7
rowMax = 7

#define some colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


msleep = lambda x: time.sleep(x / 1000.0)

sense.clear()  # no arguments defaults to off
sense.clear(red)  # passing in an RGB tuple
msleep(100)
sense.clear(green)  # passing in an RGB tuple
msleep(100)
sense.clear(blue)  # passing in an RGB tuple
msleep(100)
sense.clear()  # no arguments defaults to off


def move_pixel(pix):
    r = pix[0]
    g = pix[1]
    b = pix[2]
    
    # examples using (x, y, pixel)
    sense.set_pixel(0, 0, red)
    sense.set_pixel(0, 0, green)
    sense.set_pixel(0, 0, blue)
    


    
def pixel_stream (thecolor):
    columnIndex = 0
    rowIndex = 0
    pixelIndex = 0

    for pixelIndex in pixelFrame:
        #rowIndex += 1
        
        if columnIndex >= 8:
            columnIndex = 0
            rowIndex += 1
            
        if rowIndex >= 8:
            rowIndex = 0
            #columnIndex += 1
            

            
        sense.set_pixel(rowIndex, columnIndex, thecolor)
        
        msleep(100)
        print ("col: ", columnIndex, " row: ", rowIndex)
        columnIndex += 1




    
    

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

    
def next_pixel(pix):
    r = pix[0]
    g = pix[1]
    b = pix[2]
    
    if (r >= 255):
        #r += 1
        sense.clear()  # no arguments defaults to off
        

        
    pix[0] = r
    pix[1] = g
    pix[2] = b

#pixel_stream(red)
#pixel_stream(green)
#pixel_stream(blue)

pixelIndex = 0
for pixelLoop in pixelFrame:
    pixelIndex += 1
    print("Index: ", pixelIndex)
    


#while True:
#    for pix in pixelFrame:
#        next_pixel(pix)
#
#    sense.set_pixels(pixelFrame)
#    msleep(2)
