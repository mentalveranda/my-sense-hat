#!/usr/bin/python
#
# Source: http://pythonhosted.org/sense-hat/api/
#
# File: get_temperature.py
#
# Description: 
#   Calls get_temperature_from_humidity.
#
# Returns: 
#   Float - The current temperature in degrees Celsius.


from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature()
print("Temperature: %s C" % temp)

# alternatives
print(sense.temp)
print(sense.temperature)
