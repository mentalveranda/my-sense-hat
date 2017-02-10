#!/usr/bin/python
#
# Source: http://pythonhosted.org/sense-hat/api/
#
# File: get_temperature_from_humidity.py
#
# Description: 
#   Gets the current temperature in degrees Celsius from the humidity sensor.
#
# Returns: 
#   Float - The current temperature in degrees Celsius.


from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature_from_humidity()
print("Temperature: %s C" % temp)

