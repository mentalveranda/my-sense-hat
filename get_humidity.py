#!/usr/bin/python
#
# Source: http://pythonhosted.org/sense-hat/api/
#
# File: get_humidity.py
#
# Description: 
#   Gets the percentage of relative humidity from the humidity sensor.
#
# Returns: 
#   Float - The percentage of relative humidity.

from sense_hat import SenseHat

sense = SenseHat()
humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity)

# alternatives
print(sense.humidity)

