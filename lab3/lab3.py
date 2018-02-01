#!/usr/bin/env python
"""
Created on Tue Jan 30 12:03:54 2018

@author: Mick
"""
import spaceWaster1, spaceWaster2, spaceWaster3, spaceWaster4
from matplotlib import pyplot as plt


plt.close('all')


# %% Problem 1: sine curve plotting
sine_x, sine_y, x_lim, y_lim = spaceWaster1.sineCurve()

plt.figure('Problem 1')
plt.plot(sine_x, sine_y)
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.xlabel('x')
plt.ylabel('y')
plt.title('A sine curve')
plt.show()


# %% Problem 2: random histogram
random_sum_list = spaceWaster2.randomSumList()

plt.figure('Problem 2')
plt.hist(random_sum_list, edgecolor='k', linewidth=1)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Hopefully Normal Distribution')
plt.show()


# %% Problem 3: mass spring damper
t, position, x_lim, y_lim = spaceWaster3.SMD()

plt.figure('Problem 3')
plt.plot(t, position)
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Mass Spring Damper System')
plt.show()


# %% Problem 4: sort and sum times
length, time_sort, time_sum = spaceWaster4.timeStuff()

plt.figure('Problem 4')
plt.loglog(length, time_sort, 'd-', label='sorted()', linewidth=0.25,
           markerfacecolor='none')
plt.loglog(length, time_sum, 'x-', label='sum()', linewidth=0.25)
plt.legend()
plt.xlabel('List length')
plt.ylabel('Time')
plt.title('Comparison of sorted() and sum()')
