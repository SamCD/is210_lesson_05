#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating boolean to string function"""

def bool_to_str(bvalue, short=False):
    """Converts a boolean value into a string"""
    if bvalue is True:
        bvalue = "Yes"
    else:
        bvalue = "No"

    return bvalue if short is False else bvalue.upper()[0]
