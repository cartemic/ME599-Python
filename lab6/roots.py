#!/usr/bin/env python
"""
Created on Tue Feb 20 10:54:00 2018

@author: cartemic
"""

from complex import Complex
from math import sqrt


def roots(a, b, c):
    inner = b**2 - 4. * a * c
    twoA = 2. * a

    # define output as a set to eliminate non-unique roots
    x = set()
    if inner < 0:
        root = sqrt(abs(inner))
        x.add(Complex(-b / twoA, root / twoA))
        x.add(Complex(-b / twoA, -root / twoA))
    else:
        x.add((-b + sqrt(inner)) / twoA)
        x.add((-b - sqrt(inner)) / twoA)

    return tuple(sorted(x))


if __name__ == '__main__':
    # compare against http://www.purplemath.com/modules/complex3.htm
    print(roots(1, -2, -3))     # should return -1, 3
    print(roots(1, -6, 9))      # should return 3
    print(roots(1, 3, 3))       # should return -1.5 +/- 0.866i
