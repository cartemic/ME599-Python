#!/usr/bin/env python
"""
Created on Tue Feb 13 15:56:42 2018

@author: cartemic
"""

import numpy as np


def Verify(my_complex, python_complex):
    if my_complex.re == python_complex.real\
       and my_complex.im == python_complex.imag:
        return 'ok'
    else:
        return 'bad'


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

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        try:
            return Complex(self.re + other.re, self.im + other.im)
        except:
            return self + Complex(other)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return Complex(-self.re, -self.im)

    def __rsub__(self, other):
        try:
            return other - self
        except:
            return Complex(other) - self

    def __mul__(self, other):
        try:
            # https://www2.clarku.edu/~djoyce/complex/mult.html
            x = self.re
            y = self.im
            u = other.re
            v = other.im
            return Complex((x * u - y * v), (x * v + y * u))
        except:
            return self * Complex(other)

    def __rmul__(self, other):
        return self * other

    def __div__(self, other):
        try:
            # https://www2.clarku.edu/~djoyce/complex/div.html
            x = self.re
            y = self.im
            u = other.re
            v = other.im
            return Complex((x * u + y * v) / float(u**2 + v**2),
                           (-x * v + y * u) / float(u**2 + v**2))
        except:
            return self / Complex(other)

    def __rdiv__(self, other):
        try:
            return other / self
        except:
            return Complex(other) / self

    def __invert__(self):
        return Complex(self.re, -self.im)


def Lab5_tests():
    print('LAB 5 TESTS')
    print('===========')
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


def Lab6_tests():
    print('LAB 5 TESTS')
    print('===========')

    # part 1 test
    print('Part 1:')
    print('-------')

    a = Complex(1.2, 3.4)
    print(a)
    print('Real: {0}'.format(a.re))
    print('Imag: {0}'.format(a.im))
    print('')

    # part 2 test
    print('Part 2:')
    print('-------')

    a = Complex(1, 2)
    b = Complex(3, 4)
    a1 = complex(a.re, a.im)
    b1 = complex(b.re, b.im)
    print 'addition:',\
        Verify(a + b, a1 + b1),\
        Verify(a + 1, a1 + 1),\
        Verify(1 + a, 1 + a1)

    print 'subtraction:',\
        Verify(a - b, a1 - b1),\
        Verify(a - 1, a1 - 1),\
        Verify(1 - a, 1 - a1),\
        '\n'

    # part 3 test
    print('Part 3:')
    print('-------')
    print 'multiplication:',\
        Verify(a * b, a1 * b1),\
        Verify(a * 2, a1 * 2),\
        Verify(2 * a, 2 * a1)

    print 'division:',\
        Verify(a / b, a1 / b1),\
        Verify(a / 2, a1 / 2),\
        Verify(2 / a, 2 / a1),\
        '\n'

    print('Part 4:')
    print('-------')
    print 'negation:',\
        Verify(-a, -a1)

    print 'conjugate: ',\
        Verify(~a, a1.conjugate())


if __name__ == '__main__':
    Lab5_tests()
    Lab6_tests()
