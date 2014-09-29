#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides loan management features."""

import decimal

RATE = None
TOTAL = None

def get_interest_rate(PRINCIPAL, DURATION, PREQUALIFICATION):
    """Calculates Interest rate)"""
    RATE = None
    if PRINCIPAL >= 0 and PRINCIPAL <= 199999:
        if DURATION >= 1 and DURATION <= 15:
            if PREQUALIFICATION:
                RATE = '0.0363'
            else:
                RATE = '0.0465'
        elif DURATION >= 16 and DURATION <= 20:
            if PREQUALIFICATION:
                RATE = '0.0404'
            else:
                RATE = '0.0498'
        elif DURATION >= 21 and DURATION <= 30:
            if PREQUALIFICATION:
                RATE = '0.0577'
            else:
                RATE = '0.0639'
    elif PRINCIPAL >= 200000 and PRINCIPAL <= 999999:
        if DURATION >= 1 and DURATION <= 15:
            if PREQUALIFICATION:
                RATE = '0.0302'
            else:
                RATE = '0.0398'
        elif DURATION >= 16 and DURATION <= 20:
            if PREQUALIFICATION:
                RATE = '0.0327'
            else:
                RATE = '0.0408'
        elif DURATION >= 21 and DURATION <= 30:
            if PREQUALIFICATION:
                RATE = '0.0466'
    elif PRINCIPAL >= 1000000:
        if DURATION >= 1 and DURATION <= 15:
            if PREQUALIFICATION:
                RATE = '0.0205'
        elif DURATION >= 16 and DURATION <= 20:
            if PREQUALIFICATION:
                RATE = '0.0262'
    if RATE is not None:
        return decimal.Decimal(RATE)
    else:
        return None

def compound_interest(PRINCIPAL, DURATION, RATE=None, INTERVAL=12):
    """Calculates compound interest"""
    if RATE is not None:
        RATE = decimal.Decimal(RATE)
        TOTAL = PRINCIPAL * ((1 + RATE / INTERVAL) ** (INTERVAL * DURATION))
    return decimal.Decimal(TOTAL)

def calculate_total(PRINCIPAL,DURATION,PREQUALIFICATION):
    """Calculates total owed on a loan"""
    RATE=get_interest_rate(PRINCIPAL,DURATION,PREQUALIFICATION)
    if RATE is not None:
        TOTAL = compound_interest(PRINCIPAL,DURATION,decimal.Decimal(RATE))
        TOTAL = int(round(TOTAL))
        return TOTAL
    else:
        return None

def calculate_interest(PRINCIPAL,DURATION,PREQUALIFICATION):
    TOTAL = calculate_total(PRINCIPAL,DURATION,PREQUALIFICATION)
    if TOTAL is not None:
        INTEREST=TOTAL - PRINCIPAL
        return INTEREST
    else:
        return None
