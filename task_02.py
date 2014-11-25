#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides loan management features."""

import decimal

RATE = None
TOTAL = None


def get_interest_rate(principal, duration, prequalification):
    """Calculates Interest rate)"""
    rate = None
    if principal >= 0 and principal <= 199999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0363'
            else:
                rate = '0.0465'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0404'
            else:
                rate = '0.0498'
        elif duration >= 21 and duration <= 30:
            if prequalification:
                rate = '0.0577'
            else:
                rate = '0.0639'
    elif principal >= 200000 and principal <= 999999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0302'
            else:
                rate = '0.0398'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0327'
            else:
                rate = '0.0408'
        elif duration >= 21 and duration <= 30:
            if prequalification:
                rate = '0.0466'
    elif principal >= 1000000:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0205'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0262'
    if rate is not None:
        ret = decimal.Decimal(rate)
    else:
        ret = None
    return ret


def compound_interest(principal, duration, rate=None, interval=12):
    """Calculates compound interest"""
    if rate is not None:
        rate = decimal.Decimal(rate)
        total = principal * ((1 + rate / interval) ** (interval * duration))
    return decimal.Decimal(total)


def calculate_total(principal, duration, prequalification):
    """Calculates total owed on a loan"""
    rate = get_interest_rate(principal, duration, prequalification)
    if rate is not None:
        total = compound_interest(principal, duration, decimal.Decimal(rate))
        total = int(round(total))
    else:
        total = None
    return total


def calculate_interest(principal, duration, prequalification):
    """Calculates just the interest owed on a loan"""
    total = calculate_total(principal, duration, prequalification)
    if total is not None:
        interest = total - principal
    else:
        interest = None
    return interest
