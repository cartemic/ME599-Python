#!/usr/bin/env python
"""
Created on Tue Feb 13 15:56:42 2018

@author: cartemic
"""

import numpy as np


class Complex:
    def __init__(self, real_part=0, imaginary_part=0):
        self.re = real_part
        self.im = imaginary_part

    def __str__(self):
        if self.im < 0:
            sign = '-'
        else:
            sign = '+'
        return '({0} {1} {2}i)'.format(self.re,
                                       sign,
                                       np.abs(self.im))


if __name__ == '__main__':
    a = Complex(1.0, 2.3)
    b = Complex(2)
    c = Complex()
    d = Complex(1, -2)

    print(a)
    print(b)
    print(c)
    print(d)
