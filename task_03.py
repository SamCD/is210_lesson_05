#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates functions for converting between F and C"""


def celsius_to_fahrenheit(temperature):
    """Converts Celsius to Fahrenheit"""
    tempf = ((9 * temperature) / 5) + 32
    return float(tempf)


def fahrenheit_to_celsius(temperature):
    """Converts Fahrenheit to Celsius"""
    tempc = (5 * (temperature - 32)) / 9
    return float(tempc)


def convert_temperature(temperature, output_format='c'):
    """Conversion between Celsius and Fahrenheit"""
    if str(output_format).lower() == 'c':
        if str(temperature)[-1].lower() == 'c':
            ret = float(temperature[:-1])
        elif str(temperature)[-1].lower() == 'f':
            temp = fahrenheit_to_celsius(float(temperature[:-1]))
            ret = float(temp)
        else:
            ret = None
    elif str(output_format).lower() == 'f':
        if str(temperature)[-1].lower() == 'f':
            ret = float(temperature[:-1])
        elif str(temperature)[-1].lower() == 'c':
            temp = celsius_to_fahrenheit(float(temperature[:-1]))
            ret = float(temp)
        else:
            ret = None
    else:
        ret = None
    return ret
