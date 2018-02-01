#!/usr/bin/env python
"""
Created on Thu Feb 01 11:07:16 2018

@author: cartemic
"""

import numpy as np
import timeit
from random import random

def timeStuff():
    length = np.power(10, xrange(7))
    time_sort = []
    time_sum = []
    
    # choose the number of times to repeat in timeit function
    
    for l in length:
        theList = [random() for i in xrange(l)]
    
        # test functions and collect execution time
        t_0 = timeit.default_timer()
        sorted(theList)
        t_1 = timeit.default_timer()
        sum(theList)
        t_2 = timeit.default_timer()
    
        # append results
        time_sort.append(t_1 - t_0)
        time_sum.append(t_2 - t_1)

    return length, time_sort, time_sum
