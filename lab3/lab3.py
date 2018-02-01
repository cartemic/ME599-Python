#!/usr/bin/env python
"""
Created on Tue Jan 30 12:03:54 2018

@author: Mick
"""

import numpy as np
from matplotlib import pyplot as plt
from random import random
from msd import MassSpringDamper
import time


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
plt.show()


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


# %% Problem 3: mass spring damper

smd = MassSpringDamper(m=10.0, k=10.0, c=1.0)
state, t = smd.simulate(0.0, 1.0)
plt.figure('Problem 3')
plt.plot(t, state[:, 0])
plt.xlim([min(t), max(t)])
plt.ylim([min(state[:, 0]), max(state[:, 0])])
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Mass Spring Damper System')
plt.show()

# %% Problem 4: sort and sum times
length = np.power(10, xrange(7))
time_sort = []
time_sum = []
for l in length:
    print('List length {0}'.format(l))
    theList = [random() for i in xrange(l)]

    # test functions
    time_0 = time.time()
    sorted(theList)
    time_1 = time.time()
    sum(theList)
    time_2 = time.time()

    # output results
    time_sort.append(time_1-time_0)
    time_sum.append(time_2-time_1)
    print('Sorted time: {:0.25e} s'.format(time_1-time_0))
    print('Sum time:    {:0.25e} s'.format(time_2-time_1))
    print('')
plt.figure('Problem 4')
plt.semilogx(length, time_sort, label='sorted()')
plt.semilogx(length, time_sum, label='sum()')
plt.legend()
plt.xlabel('List length')
plt.ylabel('Time')
plt.title('Comparison of sorted() O(log(n)) and sum() O(n)')
