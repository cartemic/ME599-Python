#!/usr/bin/env python
"""
Created on Tue Jan 30 12:03:54 2018

@author: Mick
"""

import numpy as np
from matplotlib import pyplot as plt
from random import random
from msd import MassSpringDamper
import timeit


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

# choose the number of times to repeat in timeit function
num_repeats = 20

for l in length:
    print('List length {0}'.format(l))
    theList = [random() for i in xrange(l)]

    # test functions and collect average execution time
    sort_timer = timeit.Timer('sorted(theList)',
                              'from __main__ import theList')\
                              .timeit(num_repeats)/num_repeats
    sum_timer = timeit.Timer('sum(theList)',
                             'from __main__ import theList')\
                             .timeit(num_repeats)/num_repeats

    # append results and output to console
    time_sort.append(sort_timer)
    time_sum.append(sum_timer)
    print('Sorted time: {:0.3e} s'.format(sort_timer))
    print('Sum time:    {:0.3e} s'.format(sum_timer))
    print('')

# plot results
plt.figure('Problem 4')
plt.loglog(length, time_sort, 'd-', label='sorted()', linewidth=0.25,
           markerfacecolor='none')
plt.loglog(length, time_sum, 'x-', label='sum()', linewidth=0.25)
plt.legend()
plt.xlabel('List length')
plt.ylabel('Time')
plt.title('Comparison of sorted() and sum()')
