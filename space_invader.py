#!/usr/bin/env python
from sense_hat import SenseHat
from time import sleep
red = (255, 0, 0)

sense = SenseHat()
sense.clear()
sense.clear(red)  # passing in an RGB tuple
sleep(1)

sense.set_rotation(90)

sense.load_image("space_invader.png")
sleep(1)

sense.set_rotation(180)

#sense.load_image("space_invader.png")
sleep(1)

sense.set_rotation(270)

#sense.load_image("space_invader.png")
sleep(1)
sense.set_rotation(0)

#sense.load_image("space_invader.png")
sleep(1)

#sense.set_rotation(180)
# alternatives
#sense.rotation = 180
#sense.clear()

#sleep(1)

#sleep(1)


sense.clear()
