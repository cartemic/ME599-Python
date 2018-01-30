#!/usr/bin/env python
"""
Created on Tue Jan 23 13:46:51 2018

@author: Mick
"""

import math


def estimate_pi(acceptableError=1e-15, maxIterations=20, returnLast=False):
    k = -1
    lastTerm = 1000.
    estimate = 0
    factor = (2 * math.sqrt(2)) / 9801.
    while lastTerm >= acceptableError:
        k += 1
        if k < maxIterations:
            # compute pi
            lastTerm = factor * (math.factorial(4 * k) * 1103 + 26390 * k) /\
                       (math.factorial(k)**(4) * 396**(4 * k))
            estimate += lastTerm
            
        else:
            print('No convergence within tolerance and iteration limits')
            return None

    if returnLast:
        return 1/estimate, lastTerm
    else:
        return 1/estimate


if __name__ == "__main__":
    """
    test stuff
    """
    print(estimate_pi())
    print(estimate_pi(returnLast=True))
    print(math.pi)
