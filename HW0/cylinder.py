#!/usr/bin/env python


import numpy as np

# given inputs
height = 5.
radius = 3.

# calculate volume and print to console
volume = np.pi * radius**2 * height
print('Cylinder volume is {:.2f} cubic units'.format(volume))