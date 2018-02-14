#!/usr/bin/env python
"""
Created on Tue Feb 13 15:56:42 2018

@author: cartemic
"""

import numpy as np


class Complex:
    def __init__(self, real_part=0, imaginary_part=0):
        try:
            float(real_part)
            float(imaginary_part)
            self.re = real_part
            self.im = imaginary_part
        except (ValueError, TypeError) as e:
            self.re = np.nan
            self.im = np.nan
            print('Bad input, try again (' + e.__class__.__name__ + ')')

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
    e = Complex('a')
    f = Complex([1, 4])

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
