#!/usr/bin/env python
"""
Created on Tue Jan 23 13:39:27 2018

@author: Mick
"""


def gcd(a, b):
    """
    Calculates greatest common divisor using Euclid's method, as found on
    Wikipedia (https://en.wikipedia.org/wiki/Greatest_common_divisor)
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    """
    test stuff
    """
    print(gcd(6, 0))
    print(gcd(0, 6))
    print(gcd(120, 80))
    print(gcd(80, 120))
    print(gcd(7.5, 18))
