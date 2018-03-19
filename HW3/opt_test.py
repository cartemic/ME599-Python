#!/usr/bin/env python
"""
Created on Fri Mar 16 15:04:39 2018

@author: cartemic
"""

import numpy as np
from scipy import interpolate as spi
from scipy import optimize as spo
import multiprocessing as mp


waypoints_mid = mp.Array('d', 2)
waypoints = [[-10, -10], [0, 0], [10, 10]]


# line function
def line(x, m, sim, best_score, waypoints_mid, record_waypoints):

    waypoints[1] = [x, m * x]
    score = sim.evaluate(waypoints)
    if score < best_score.value:
        best_score.value = score
        waypoints_mid[0] = x
        waypoints_mid[1] = m * x
        record_waypoints([waypoints[0],
                         waypoints_mid[:],
                         waypoints[2]])

    return score


def spline_optimizer(m, sim, best_score, waypoints_mid, record_waypoints):
    num_line_points = 10
    x_max = min(10, abs(10./m))
    x_min = -x_max
    x_locations = np.linspace(x_min,
                              x_max,
                              num_line_points)

    # get a set of scores along a line
    scores = np.array([line(x,
                            m,
                            sim,
                            best_score,
                            waypoints_mid,
                            record_waypoints) for x in x_locations])
    spline = spi.UnivariateSpline(x_locations, scores)
    minimum = spo.differential_evolution(spline, [(x_min, x_max)], disp=False)
    line(minimum.x[0],
         m,
         sim,
         best_score,
         waypoints_mid,
         record_waypoints)


def optimize(sim, record_waypoints, done):
    best_score = mp.Value('d', sim.evaluate(waypoints))
    num_cores = mp.cpu_count()
    slopes = np.tan(np.linspace(np.pi/4, 9*np.pi/4, 16)[:-1])
    processes = [mp.Process(target=spline_optimizer,
                            args=[m,
                                  sim,
                                  best_score,
                                  waypoints_mid,
                                  record_waypoints])
                 for m in slopes]
    [setattr(p, 'is_open', False) for p in processes]

    for p in processes[0:num_cores]:
        p.is_open = True
        p.start()

    stop = False
    collected = 0
    started = len(processes)
    while not stop and not done():
        for i, p in enumerate(processes):
            open_new = False
            if p.is_open is True and p.is_alive() is False:
                p.join()
                open_new = True

            if open_new:
                index = [i for i, p2 in enumerate(processes)
                         if p2.is_open is False]
                if len(index) > 0:
                    processes[index[0]].is_open = True
                    processes[index[0]].start()
                    open_new = False

        if collected == started:
            stop = True
