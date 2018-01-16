#!/usr/bin/env python
"""
Created on Tue Jan 16 12:06:38 2018

@author: Mick
"""

import numpy as np

def cylinder_volume(radius, height):
# calculate cylinder volume from user inputs
    return(np.pi * radius**2 * height)

if __name__ == "__main__":
    # enter test conditions
    height = 5.
    radius = 3.
    print(cylinder_volume(radius, height))
