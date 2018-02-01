#!/usr/bin/env python
"""
Created on Thu Feb 01 10:52:18 2018

@author: cartemic
"""

import numpy as np


def sineCurve():
    sine_x = np.linspace(0, 4*np.pi, 100)
    sine_y = np.sin(sine_x)

    x_lim = [min(sine_x), max(sine_x)]
    y_lim = [min(sine_y), max(sine_y)]

    return sine_x, sine_y, x_lim, y_lim
