#!/usr/bin/env python
"""
Created on Tue Feb 06 11:53:19 2018

@author: cartemic
"""

import sys

if len(sys.argv) < 3:
    print('Two arguments is the minimum requirement for a nutritious function')
else:
    if len(sys.argv) > 3:
        print('I\'m ignoring everything but your first two arguments')
    print(sys.argv[1])
    print(sys.argv[2])