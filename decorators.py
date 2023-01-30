"""
Author: Damian Archer
Date: 1/17/2023
File: decorators.py
Purpose: PCPP Exercises - Decorators
"""

import time
import calendar
import datetime

def timestamper(process):
    def wrapper(a,b):
        print("{} performing {} on {} and {}".format(get_timestamp(), process.__name__, a, b))
        process(a,b)
        print("{} completed {} on {} and {}".format(get_timestamp(), process.__name__, a, b))
    return wrapper

def get_timestamp():
    return datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

@timestamper
def addition(a,b):
    return a+b

@timestamper
def multiplication(a,b):
    return a*b

@timestamper
def subtraction(a,b):
    return a-b

addition(1,3)
multiplication(2,3)
subtraction(3,3)

            



        
