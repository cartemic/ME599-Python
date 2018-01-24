#!/usr/bin/env python
"""
Created on Tue Jan 16 12:43:35 2018

@author: Mick
"""


def close(num1, num2, num3):
    """
    Takes three numbers as arguments and returns True if the absolute
    difference between the first two numbers is less than the third number.
    """
    if abs(num1 - num2) < num3:
        return(True)
    else:
        return(False)


if __name__ == "__main__":
    # test stuff
    print(close(1, 2, 3))
    print(close(1, 7, 1))
