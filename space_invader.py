#!/usr/bin/env python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

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
