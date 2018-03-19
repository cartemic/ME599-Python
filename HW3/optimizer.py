#!/usr/bin/env python
"""
Created on Fri Mar 16 15:04:39 2018

@author: cartemic

PLEASE do not run in ipython, as it seems to have a hard time with the
multiprocessing module somehow.
"""

import numpy as np
from scipy import interpolate as spi
from scipy import optimize as spo
import multiprocessing as mp
import os


# make shared-memory array for multiprocessing
waypoints_mid = mp.Array('d', 2)


def add_point(point):
    # add a waypoint to the basic points
    return [[-10, -10], point, [10, 10]]


def line(x, m, sim, best_score, waypoints_mid, record_waypoints):
    # calculates a y value based on a slope and x value
    # all lines pass through the origin
    my_points = add_point([x, m * x])
    score = sim.evaluate(my_points)

    # update current values if it is good
    if score < best_score.value:
        best_score.value = score
        waypoints_mid[0] = x
        waypoints_mid[1] = m * x
        record_waypoints(my_points)

    return score


def random_optimizer(sim, best_score, waypoints_mid, record_waypoints, done):
    while not done.value:
        # find some random points
        x = np.random.uniform(20) - 10.
        y = np.random.uniform(20) - 10.
        my_points = add_point([x, y])
        score = sim.evaluate(my_points)

        # update current values if they are good
        if score < best_score.value:
            best_score.value = score
            waypoints_mid[0] = x
            waypoints_mid[1] = y
            record_waypoints(my_points)


def spline_optimizer(m, sim, best_score, waypoints_mid, record_waypoints):
    # define number of points to sample and x range
    num_line_points = 10
    x_max = min(10, abs(10./m))
    x_min = -x_max
    x_locations = np.linspace(x_min,
                              x_max,
                              num_line_points)

    # get a set of scores along the line
    scores = np.array([line(x,
                            m,
                            sim,
                            best_score,
                            waypoints_mid,
                            record_waypoints) for x in x_locations])

    # fit a spline to simulation results
    spline = spi.UnivariateSpline(x_locations, scores)

    # locate the estimated minimum of the spline on the interval and return
    # the score for the corresponding x location
    minimum = spo.differential_evolution(spline, [(x_min, x_max)], disp=False)
    line(minimum.x[0],
         m,
         sim,
         best_score,
         waypoints_mid,
         record_waypoints)


def optimize(sim, record_waypoints, done):
    # define a shared value for the best score and done() output
    best_score = mp.Value('d', sim.evaluate(add_point([0, 0])))
    shared_done = mp.Value('i', 0)

    # figure out how many cores are available
    num_cores = mp.cpu_count()

    # array of slopes for lines:
    #    start with a line from (-10, 10) to (10, -10) and rotate it about
    #    the origin. Some points will be sampled on each line (defined in the
    #    spline optimizer) and a location of minimum score will be estimated.
    slopes = np.tan(np.linspace(np.pi/4, 9*np.pi/4, 16)[:-1])

    # make a process for the dumb optimizer, just in case it performs well
    processes = [mp.Process(target=random_optimizer,
                            args=[sim,
                                  best_score,
                                  waypoints_mid,
                                  record_waypoints,
                                  shared_done])]

    # make a process for running the spline optimizer on each slope
    processes += [mp.Process(target=spline_optimizer,
                             args=[m,
                                   sim,
                                   best_score,
                                   waypoints_mid,
                                   record_waypoints])
                  for m in slopes]

    # add an attribute to each process to figure out whether it is open. This
    # is used to open a new process only when a new core becomes available.
    [setattr(p, 'is_open', False) for p in processes]

    # start a process on each core
    for p in processes[0:num_cores]:
        p.is_open = True
        p.start()

    while not done():
        # just-in-case recording of waypoints, since it seems to only work
        # on occasion and troubleshooting multiple simultaneous processes
        # suuuuuuucks
        record_waypoints(add_point(waypoints_mid[:]))

        # decide whether or not to join the process and open a new one
        for i, p in enumerate(processes):
            open_new = False
            if i != 0 and p.is_open is True and p.is_alive() is False:
                p.join()
                open_new = True

            # open a new process
            if open_new:
                index = [i for i, p2 in enumerate(processes)
                         if p2.is_open is False]
                if len(index) > 0:
                    processes[index[0]].is_open = True
                    processes[index[0]].start()
                    open_new = False

    # end random point guesser
    shared_done.value = 1

    # clean up processes
    [p.terminate() for p in processes if p.is_alive()]

    # clean non-deleted files from directory
    for f in os.listdir('./'):
        if 'waypoints-' in f:
            try:
                os.remove(f)
            except WindowsError:
                pass
