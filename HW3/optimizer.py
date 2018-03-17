#!/usr/bin/env python
"""
Created on Thu Mar 15 12:23:13 2018

@author: cartemic
"""

import random as random
from scipy import optimize as spo
from scipy import interpolate as spi
import numpy as np
from matplotlib import pyplot as plt


def optimize_lines(sim, record_waypoints, done):
    # get basic score
    waypoints = np.array([[-10, -10], [0, 0], [10, 10]])
    best_score = sim.evaluate(waypoints)

    # line function
    def line(x, m=-1, record=False):
        if m is None:
            waypoints[1] = [0, x]
        else:
            waypoints[1] = [x, m * x]
        return sim.evaluate(waypoints)

    # build a line to fit
    num_line_points = 100
    slopes = [-1, 0, None]
    x_locations = np.linspace(-10, 10, num_line_points)
    splines = []
    for m in slopes:
        scores = np.array([line(x, m) for x in x_locations])
        splines.append(spi.UnivariateSpline(x_locations, scores))
        minimum = spo.brute(splines[-1], [(-10, 10)])
        print 'x:', minimum[0]
        print 'actual score:', line(minimum[0])


def optimize_chk(sim, record_waypoints, done=False):
    base_waypoints = [(-10, -10), (10, 10)]
    base_score = sim.evaluate(base_waypoints)

    new_waypoints = base_waypoints[:]
    new_waypoints.insert(1, [0, 0])
    new_waypoints.insert(1, [0, 0])
    num_check_points = 50
    scores_x = []
    scores_y = []
    for i in xrange(num_check_points):
        new_waypoints[1][0] = ((i + 1) / float(num_check_points)) * 20 - 10
        new_waypoints[1][1] = -10
        new_waypoints[2][0] = new_waypoints[1][0]
        new_waypoints[2][1] = 10

        scores_x.append(sim.evaluate(new_waypoints))

        new_waypoints[1][0] = -10
        new_waypoints[1][1] = ((i + 1) / float(num_check_points)) * 20 - 10
        new_waypoints[2][0] = 10
        new_waypoints[2][1] = new_waypoints[1][1]

        scores_y.append(sim.evaluate(new_waypoints))

    return np.linspace(-10, 10, num_check_points), scores_x, scores_y


def optimize(sim, record_waypoints, done):
    base_waypoints = [(-10, -10), (10, 10)]
    best_score = sim.evaluate(base_waypoints)

    new_waypoints = base_waypoints[:]
    new_waypoints.insert(1, [0, 0])

    while not done():
        test_waypoints = new_waypoints[:]
        test_waypoints[1][0] = random.random() * 20 - 10
        test_waypoints[1][1] = random.random() * 20 - 10
        test_score = sim.evaluate(new_waypoints)
        if test_score < best_score:
            best_score = test_score
            new_waypoints = test_waypoints[:]
            record_waypoints(new_waypoints)


def optimize_buthow(sim, record_waypoints, done=False):
    base_waypoints = [(-10, -10), (10, 10)]
    base_score = sim.evaluate(base_waypoints)

    new_waypoints = base_waypoints[:]
    new_waypoints.insert(1, [0, 0])

    def tester(args):
        new_waypoints[1][0] = args[0]
        new_waypoints[1][1] = args[1]
        return sim.evaluate(new_waypoints)

    guess = [0, 0]

    while not done:
        spo.basinhopping(tester, (0, 0))


def optimize_eps(sim, record_waypoints, done):
    num_waypoints = 3
    waypoint_step = 0.1

    # get a new random waypoint
    def new_point():
        x = random.random() * 20 - 10
        y = random.random() * 20 - 10
        return [x, y]

    waypoints_basic = [(-10, -10), (10, 10)]
    waypoints_better = waypoints_basic[:]

    waypoints_better.insert(1, [0, 0])

    basic_score = sim.evaluate(waypoints_basic)
    better_score = sim.evaluate(waypoints_better)

    new_score = [better_score, better_score]
    count = 0
    repeat_count = 0

    # generate improved waypoint file
    while not done():
        count += 1

    # %% attempt at extended pattern search, because it's neat
        improvement_indices = range(1, num_waypoints-1)
        for i in improvement_indices[:]:
            # generate index for improvement and removal
            random_index = random.randrange(len(improvement_indices))

            # improve the score using the point at random_index
            [x, y] = waypoints_better[improvement_indices[random_index]]

            # move the points
            for direction in range(4):
                if direction == 0:
                    # go right
                    x = min(x + waypoint_step, 10)
                elif direction == 1:
                    # go down
                    y = max(y - waypoint_step, -10)
                elif direction == 2:
                    # go left
                    x = max(x - waypoint_step, -10)
                else:
                    # go up
                    y = min(y + waypoint_step, 10)

                # replace current point with moved point
                waypoints_better[improvement_indices[random_index]] = (x,
                                                                       y)

                # check for score improvement
                new_score[0] = sim.evaluate(waypoints_better)
                if new_score[0] < new_score[1]:
                    # score improvement
                    record_waypoints(waypoints_better)
                    break

            # remove this point
            improvement_indices.pop(random_index)

            # cut step down if no improvement over last two runs
            if new_score[0] == new_score[1]:
                repeat_count += 1
            else:
                new_score[1] = new_score[0]

            if repeat_count == 2:
                # move point randomly
                repeat_count = 0
                improvement_count = 0
                needs_improvement = True
                original_waypoints_better = waypoints_better[:]
                while needs_improvement:
                    # generate random points
                    waypoints_better[1] = new_point()

                    # check for improvement
                    test = sim.evaluate(waypoints_better)
                    improvement_count += 1

                    if test < new_score[0]:
                        # score improvement
                        new_score[0] = test
                        record_waypoints(waypoints_better)
                        break

                    if improvement_count == 50:
                        # it got worse, reset to the original
                        waypoints_better = original_waypoints_better[:]
                        break

                # reduce step size
                waypoint_step /= 2.

    return(basic_score, new_score[0], waypoints_better)
