#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:24:07 2020

@author: john
"""

def ctof (cent):
    return str((cent*(1.8))+32)

def ftoc (fahr):
    return str((fahr-32)*(5/9))

print("Zero degrees celcius is "+ctof(0)+" Fahrenheit.")
print("Ten degrees celcius is "+ctof(10)+" Fahrenheit.")
print("Zero degrees Fahrenheit is "+ftoc(0)+" Celcius.")
print("Ten degrees Fahrenheit is "+ftoc(10)+" Celcius.")