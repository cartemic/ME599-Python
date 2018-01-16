#!/usr/bin/env python
"""
Created on Tue Jan 16 12:06:38 2018

@author: Mick
"""

import numpy as np


def cylinder_volume(radius, height):
    """
    calculates cylinder volume from user inputs
    """

    # ensure inputs aren't dumb
    if (radius < 0) or (height < 0):
        return(None)
    else:
        return(np.pi * radius**2 * height)


def torus_volume(majorRadius, minorRadius):
    """
    calculates torus volume from user inputs
    """

    # ensure inputs aren't dumb
    if (majorRadius < 0) or (minorRadius < 0):
        return(None)
    else:
        return((np.pi * minorRadius**2) * (2. * np.pi * majorRadius))


if __name__ == "__main__":
    # test cylinder for regular stuff and negative numbers
    print('cylinder test\n=============')
    height = 5. * np.array([1, 1, -1])
    radius = 3. * np.array([1, -1, 1])
    print([cylinder_volume(radius[i], height[i]) for i in range(len(height))])
    print('\n')

    # test torus regular stuff and negative numbers
    print('torus test\n==========')
    minorRadius = 3. * np.array([1, 1, -1])
    majorRadius = 4. * np.array([1, -1, 1])
    print([cylinder_volume(majorRadius[i], minorRadius[i]) for i in
           range(len(majorRadius))])
    print('\n')
