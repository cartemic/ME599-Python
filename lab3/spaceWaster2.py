#!/usr/bin/env python
"""
Created on Thu Feb 01 10:56:50 2018

@author: cartemic
"""

from random import random


def sample_random():
    return sum([random() for i in xrange(10)])


def randomSumList():
    return [sample_random() for i in xrange(10000)]
