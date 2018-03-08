#!/usr/bin/env python
"""
Created on Wed Mar 07 17:28:07 2018

@author: cartemic
"""

import numpy as np


def optimize_step(f, bounds, n):
    x_values = np.linspace(bounds[0], bounds[1], n)
    y_values = np.zeros(len(x_values))
    for i, x in enumerate(x_values):
        y_values[i] = f(x)
    return x_values[y_values == np.nanmax(y_values)][0]


def optimize_random(f, bounds, n):
    x_values = np.random.rand(n) * (bounds[1]-bounds[0]) + bounds[0]
    y_values = np.zeros(n)
    for i, x in enumerate(x_values):
        y_values[i] = f(x)
    return x_values[y_values == np.nanmax(y_values)][0]


def optimize_gradient(f, bounds, epsilon):
    pass


def optimize_md(f, bounds, cutoff=1e-6):
    ratio = (np.sqrt(5)-1)/2
    cutoff = abs(cutoff)
    dimensions = len(bounds)
    points = [[], [], [], []]
    for i in range(dimensions):
        points[0].append(bounds[i][0])
        points[3].append(bounds[i][1])

    # ensure inequality for golden ratio bracketing optimization
    if f(*points[0]) > f(*points[3]):
        points[1] = points[3][:]
        points[3] = points[0][:]
        points[0] = points[1][:]
        points[1] = []

    def get_inner():
        # gets new inner points based on outer points
        points[1] = []
        points[2] = []
        for i in range(len(points[0])):
            points[1].append(points[3][i] -
                             ratio * (points[3][i] - points[0][i]))
            points[2].append(points[0][i] +
                             ratio * (points[3][i] - points[0][i]))

    # optimize using golden ratio bracketing
    # http://csg.sph.umich.edu/abecasis/class/815.20.pdf
    # https://www.youtube.com/watch?v=lkUj-JVbQ04
    # https://www.essie.ufl.edu/~kgurl/Classes/Lect3421/NM6_optim_s02.pdf
    solutions = [f(*points[0])]
    error = 1.
    while error > cutoff:
        get_inner()
        # evaluate function
        left = f(*points[1])
        right = f(*points[2])
        # shift brackets
        if left < right:
            points[0] = points[1][:]
            solutions.append(right)
        else:
            points[3] = points[2][:]
            solutions.append(left)

        error = (1 - ratio) * np.min(np.array(points[3])-np.array(points[0]))
    return points[3]


def my_function(x):
    # inverted parabola with max of 3 at (1)
    return 3 - (x-1)**2


def my_function_md(x, y, z):
    # sphere with max of 9 at (1, 2, 3)
    return 9 - (x-1)**2 - (y-2)**2 - (z-3)**2


if __name__ == '__main__':
    # STILL NEEDED: Plots and gradient function
    print(optimize_step(my_function, (-1, 1.5), 10000))
    print(optimize_random(my_function, (-1, 1.5), 10000))
    print(optimize_md(my_function_md, ((0, 2), (1, 3), (2, 4)), 1e-10))
