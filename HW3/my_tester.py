#!/usr/bin/env python
"""
Created on Thu Mar 15 13:10:50 2018

@author: cartemic
"""

from multiprocessing import Process, Queue
from simulator import Simulator
from optimizer import optimize, optimize_chk
from matplotlib import pyplot as plt
import numpy as np
import time

s = Simulator(8)
#scores_x, scores_y = optimize_chk(s, None)
#x = np.array(range(1, len(scores_x)+1), dtype=float)
#x = x / np.max(x) * 20 - 10
#scores_x = np.array(scores_x)
#scores_y = np.array(scores_y)
#intensity = np.meshgrid(scores_x, scores_y)
#plt.contourf(x, x, intensity[0] + intensity[1])
#plt.show()


t0 = time.time()
max_time = 20

optimize(s, 0)
