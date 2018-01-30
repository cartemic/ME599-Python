#!/usr/bin/env python
"""
Created on Tue Jan 30 12:03:54 2018

@author: Mick
"""

import numpy as np
from matplotlib import pyplot as plt
from random import random

plt.close('all')


# %% Problem 1: sine curve plotting
sine_x = np.linspace(0, 4*np.pi, 100)
sine_y = np.sin(sine_x)

plt.figure('Problem 1')
plt.plot(sine_x, sine_y)
plt.xlim([min(sine_x), max(sine_x)])
plt.ylim([min(sine_y), max(sine_y)])
plt.xlabel('x')
plt.ylabel('y')
plt.title('A sine curve')


# %% Problem 2: random histogram
def sample_random():
    return sum([random() for i in xrange(10)])


random_sum_list = [sample_random() for i in xrange(10000)]
plt.figure('Problem 2')
plt.hist(random_sum_list, edgecolor='k', linewidth=1)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Hopefully Normal Distribution')
plt.show()


if __name__ == "__main__":
    """
    test stuff
    """
