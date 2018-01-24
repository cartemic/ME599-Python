#!/usr/bin/env python
"""
Created on Tue Jan 23 13:46:51 2018

@author: Mick
"""

def estimate_pi(acceptableError=1e-15, maxIterations=1e6):
    k = 0
    error = 1.
    while error >= acceptableError:
        if k < maxIterations:
            # compute pi
        else:
            print('No convergence within tolerance and iteration limits')
            return None


if __name__ == "__main__":
    """
    test stuff
    """
