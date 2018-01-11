#!/usr/bin/env python


import numpy as np

# given inputs
radius_inner = 3.
radius_outer = 4.

'''
find radii for volume formula using the formula found at:
https://en.wikipedia.org/wiki/Torus
taking "radius of the hole" to be from the top-down projection (R-r)
and "radius from the center to the edge of the shape" to be the
minor radius (r)
'''
radius_major = radius_inner + radius_outer
radius_minor = radius_outer

# calculate volume and print to console
volume = (np.pi * radius_minor**2) * (2. * np.pi * radius_major)
print('Torus volume is {:.2f} cubic units'.format(volume))