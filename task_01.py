#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bool_to_str(bvalue,short=False):
    """Converts a boolean value into a string"""
    if bvalue == True:
        bvalue = "Yes"
    else:
        bvalue = "No"

    return bvalue if short==False else bvalue.upper()[0]
