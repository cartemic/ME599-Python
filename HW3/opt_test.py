#!/usr/bin/env python
"""
Created on Fri Mar 16 15:04:39 2018

@author: cartemic
"""

import numpy as np
from simulator import Simulator
from scipy import interpolate as spi
from scipy import optimize as spo
import multiprocessing as mp
from tester import record_waypoints
import sys


waypoints = np.array([[-10, -10], [0, 0], [10, 10]])
war_lock = mp.Lock()
best_score = 1000
best_waypoints = waypoints[:]
q = mp.Queue()


# line function
def line(x, m, sim, record=False):
    global war_lock
    global best_score
    global best_waypoints

    if m is None:
        waypoints[1] = [0, x]
    else:
        waypoints[1] = [x, m * x]
    score = sim.evaluate(waypoints)

    with war_lock:
        if score < best_score:
            record_waypoints(waypoints)

    return score          


def spline_optimizer(m, sim, q):
    num_line_points = 10
    x_locations = np.linspace(-10, 10, num_line_points)

    # get a set of scores along a line
    scores = np.array([line(x, m, sim) for x in x_locations])
    spline = spi.UnivariateSpline(x_locations, scores)
    minimum = spo.differential_evolution(spline, [(-10, 10)])
    q.put((m, minimum.x[0], line(minimum.x[0], m, sim)))
    sys.stdout.flush()


if __name__ == '__main__':
    # generate a random instanceq
    instance = int(np.random.uniform(0, 1000))
    sim = Simulator(instance)
    best_score = sim.evaluate(best_waypoints)

    print 'instance', instance
    print 'base score:', best_score

    num_cores = mp.cpu_count()
    slopes = np.tan(np.linspace(np.pi/4, 9*np.pi/4, 16)[:-1])
    processes = [mp.Process(target=spline_optimizer, args=[m, sim, q])
                 for m in slopes]
    [setattr(p, 'is_open', False) for p in processes]
    
    for p in processes[0:num_cores]:
        p.is_open = True
        p.start()

    stop = False
    collected = 0
    started = len(range(num_cores))
    while not stop:
        for i, p in enumerate(processes):
            open_new = False
            if p.is_open is True and p.is_alive() is False:
                p.join()
                open_new = True

            if open_new:
                index = [i for i, p2 in enumerate(processes) if p2.is_open == False][0]
                if index != []:
                    processes[index].is_open = True
                    processes[index].start()

        if q.qsize() > 0:
            collected += 1
            print collected, q.get()

        if collected == started:
            stop = True
