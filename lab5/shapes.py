#!/usr/bin/env python
"""
Created on Tue Feb 13 15:40:45 2018

@author: cartemic
"""

import numpy as np


class Circle:
    def __init__(self, diameter):
        self.diam = float(diameter)

    def diameter(self):
        return self.diam

    def area(self):
        return np.pi / 4 * self.diam**2

    def perimeter(self):
        return np.pi * self.diam


class Rectangle:
    def __init__(self, length, width):
        try:
            float(length)
            float(width)
            self.L = length
            self.W = width
        except (ValueError, TypeError) as e:
            print('Bad input, try again (' + e.__class__.__name__ + ')')
            return(None)

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
    test_rectangle = Rectangle(4, [3, 5])
