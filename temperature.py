#!/usr/bin/env python

'''
This is a python moule that converts temptures
'''

def f_to_k(ftemp):
    converted = ((ftemp - 32.) * ( 5./9.)) +273.15
    return converted

print(f_to_k(100.))
