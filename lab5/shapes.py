#!/usr/bin/env python
"""
Created on Tue Feb 13 15:40:45 2018

@author: cartemic
"""

import numpy as np


class Circle:
    def __init__(self, diameter=0):
        try:
            float(diameter)
            if diameter < 0:
                raise ValueError
            self.diam = diameter
        except (ValueError, TypeError) as e:
            self.diam = np.nan
            print('Bad input, try again (' + e.__class__.__name__ + ')')

    def diameter(self):
        return self.diam

    def area(self):
        return np.pi / 4 * self.diam**2

    def perimeter(self):
        return np.pi * self.diam


class Rectangle:
    def __init__(self, length=0, width=0):
        try:
            float(length)
            float(width)
            if (length < 0) or (width < 0):
                raise ValueError
            self.L = length
            self.W = width
        except (ValueError, TypeError) as e:
            self.L = np.nan
            self.W = np.nan
            print('Bad input, try again (' + e.__class__.__name__ + ')')

    def area(self):
        return self.L * self.W

    def perimeter(self):
        return 2 * (self.L + self.W)


if __name__ == '__main__':
    print('            CIRCLE TEST')
    print('===================================')

    test_diameter = 2.
    test_circle = Circle(test_diameter)

    print('Circle diameter error:     {0:1.2e}'.format(test_circle.diameter() -
                                                       test_diameter))
    print('Circle area error:         {0:1.2e}'.format(test_circle.area() -
                                                       np.pi / 4 *
                                                       test_diameter**2))
    print('Circle perimeter error:    {0:1.2e}'.format(test_circle.perimeter()
                                                       - np.pi
                                                       * test_diameter))
    test_circle = Circle('a')
    test_circle = Circle(-1)
    test_circle = Circle([9, 3])
    print(test_circle.area())
    print('')

    print('           RECTANGLE TEST')
    print('===================================')

    test_L = 2
    test_W = 1
    test_rectangle = Rectangle(test_L, test_W)

    print('Rectangle area error:      {0:1.2e}'.format(test_rectangle.area() -
                                                       test_L * test_W))
    print('Rectangle perimeter error: {0:1.2e}'.format(test_rectangle
                                                       .perimeter()
                                                       - 2
                                                       * (test_L + test_W)))

    test_rectangle = Rectangle('a', 4)
    test_rectangle = Rectangle(4, 'g')
    test_rectangle = Rectangle(4, -1)
    test_rectangle = Rectangle(4, [3, 5])
    print(test_rectangle.area())
