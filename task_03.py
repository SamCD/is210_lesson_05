#!/usr/bin/env python
# -*- coding: utf-8 -*-

def celsius_to_fahrenheit(temperature):
    """Converts Celsius to Fahrenheit"""
    TEMPF=((9 * temperature) / 5) + 32
    return float(TEMPF)

def fahrenheit_to_celsius(temperature):
    """Converts Fahrenheit to Celsius"""
    TEMPC=(5 * (temperature - 32)) / 9
    return float(TEMPC)

def convert_temperature(temperature,output_format='c'):
    """Conversion between Celsius and Fahrenheit"""
    if str(output_format).lower() == 'c':
        if str(temperature)[-1].lower() == 'c':
            return float(temperature[:-1])
        elif str(temperature)[-1].lower() == 'f':
            TEMP = fahrenheit_to_celsius(float(temperature[:-1]))
            return float(TEMP)
        else:
            return None
    elif str(output_format).lower() == 'f':
        if str(temperature)[-1].lower() == 'f':
            return float(temperature[:-1])
        elif str(temperature)[-1].lower() == 'c':
            TEMP = celsius_to_fahrenheit(float(temperature[:-1]))
            return float(TEMP)
        else:
            return None
    else:
        return None
