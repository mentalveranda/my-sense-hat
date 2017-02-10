#!/usr/bin/python
#
# Source: http://pythonhosted.org/sense-hat/api/
#
# File: get_temperature_from_pressure.py
#
# Description: 
#   Gets the current temperature in degrees Celsius from the pressure sensor.
#
# Returns: 
#   Float - The current temperature in degrees Celsius.


from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature_from_pressure()
print("Temperature: %s C" % temp)

