#!/usr/bin/env python
"""
Created on Thu Feb 01 11:01:29 2018

@author: cartemic
"""

from msd import MassSpringDamper

def SMD():
    smd = MassSpringDamper(m=10.0, k=10.0, c=1.0)
    state, t = smd.simulate(0.0, 1.0)

    return t, state[:, 0], [min(t), max(t)],\
            [min(state[:, 0]), max(state[:, 0])]
