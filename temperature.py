#!/usr/bin/env python

'''
This is a python moule that converts temptures
another line here
'''

def f_to_k(ftemp):
    converted = ((ftemp - 32.) * ( 5./9.)) +273.15
    return converted


def k_to_c(ktemp):
    return ktemp - 273.15

def f_to_c(ftemp):
    return k_to_c(f_to_k(ftemp))

print(f_to_c(100.))
