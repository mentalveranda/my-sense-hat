#!/usr/bin/env python
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.load_image("space_invader.png")

sleep(1)

sense.set_rotation(180)
# alternatives
sense.rotation = 180
sense.clear()

sleep(1)

sense.load_image("space_invader.png")
sleep(1)


sense.clear()
