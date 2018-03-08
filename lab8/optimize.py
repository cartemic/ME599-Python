#!/usr/bin/env python
"""
Created on Wed Mar 07 17:28:07 2018

@author: cartemic
"""

import numpy as np
import scipy as sp
from matplotlib import pyplot as plt


plt.close('all')


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


def optimize_gradient(f, bounds, epsilon, max_iter=100000, max_loop_err=True):
    # set initial step size, h
    left = min(bounds)
    right = max(bounds)
    interval = right - left
    h = 0.1 * interval

    # generate a random point on the interval to begin evaluation
    x = np.random.uniform(left + 2 * h, right - 2 * h)
    y = np.zeros(5)

    # initialize derivative, solution, counter, and error
    count = 0

    # begin optimization
    while h > epsilon:
        count += 1

        # evaulate x over range +/- h to get derivative
        y = [f(x - 2 * h), f(x - h), f(x), f(x + h), f(x + 2 * h)]
        j = 2

        # calculate derivative using 4th order accurate central difference
        y_prime = (y[j-2] - 8 * y[j-1] + 8 * y[j+1] - y[j+2]) / (12 * h)

        h = 0.01 * y_prime
        x += h

        # do counter stuff
        if count >= max_iter:
            if max_loop_err:
                print 'ERROR: No convergence within', max_iter, 'iterations'
                return None
            else:
                break

    # return requested values
    return x


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

    def get_inner(replace, replace_with):
        if replace == replace_with:
            # use to initialize inner points
            points[1] = []
            points[2] = []
            for i in range(len(points[0])):
                points[1].append(points[3][i] - ratio * (points[3][i] -
                                                         points[0][i]))
                points[2].append(points[0][i] + ratio * (points[3][i] -
                                                         points[0][i]))
            return

        # gets new inner points based on outer points
        points[replace] = points[replace_with][:]
        points[replace_with] = []
        if replace < replace_with:
            # replace left inner point
            for i in range(len(points[0])):
                points[replace_with].append(points[3][i] -
                                            ratio * (points[3][i] -
                                                     points[0][i]))
        else:
            # replace right inner point
            for i in range(len(points[0])):
                points[replace_with].append(points[0][i] +
                                            ratio * (points[3][i] -
                                                     points[0][i]))

    # optimize using golden ratio bracketing
    # http://csg.sph.umich.edu/abecasis/class/815.20.pdf
    # https://www.youtube.com/watch?v=lkUj-JVbQ04
    # https://www.essie.ufl.edu/~kgurl/Classes/Lect3421/NM6_optim_s02.pdf
    solutions = [f(*points[0])]
    error = 1.
    while error > cutoff:
        get_inner(0, 0)
        # evaluate function
        left = f(*points[1])
        right = f(*points[2])
        # shift brackets
        if left < right:
            points[0] = points[1][:]
            get_inner(1, 2)
            solutions.append(right)
        else:
            points[3] = points[2][:]
            points[2] = points[1][:]
            solutions.append(left)

        error = (1 - ratio) * np.min(np.array(points[3])-np.array(points[0]))
    return points[3]


def my_function(x):
    # inverted parabola with max of 3 at (1)
    return 3 - (x-1)**2


def my_function_md(x, y, z):
    # sphere with max of 9 at (1, 2, 3)
    return 9 - (x-1)**2 - (y-2)**2 - (z-3)**2


def check_functions():
    print 'SHOULD RETURN A VALUE OF 1'
    print ' STEP:    ', optimize_step(my_function, (-1, 1.5), 10000)
    print ' RANDOM:  ', optimize_random(my_function, (-1, 1.5), 10000)
    print ' GRADIENT:', optimize_gradient(my_function, (-1, 1.5),
                                          1e-16, 10000, False)
    print
    print 'SHOULD RETURN 1, 2, 3'
    print ' MULTI:   ', optimize_md(my_function_md, ((0, 2), (1, 3), (2, 4)),
                                    1e-10)


def plot_functions():
    solution = 1.
    steps = np.logspace(2, 12, 50, base=2)
    # use lambda function to maximize rather than minimize the function
    # https://stackoverflow.com/questions/10146924/
    # finding-the-maximum-of-a-function
    builtin_err = abs(solution -
                      sp.optimize.minimize(lambda x: -my_function(x),
                                           0).x[0]) * np.ones(steps.shape)
    step_err = np.array([abs(optimize_step(my_function,
                                           (-1, 1.5),
                                           int(step)) - solution)
                         for step in steps])
    rand_err = np.array([abs(optimize_random(my_function,
                                             (-1, 1.5),
                                             int(step)) - solution)
                         for step in steps])
    grad_err = np.array([abs(optimize_gradient(my_function,
                                               (-1, 1.5),
                                               0,
                                               int(step),
                                               False) - solution)
                         for step in steps])
    plt.semilogx(steps, builtin_err, label='Scipy', basex=2, linewidth=0.5)
    plt.semilogx(steps, step_err, label='Step', basex=2, linewidth=0.5)
    plt.semilogx(steps, rand_err, label='Random', basex=2, linewidth=0.5)
    plt.semilogx(steps, grad_err, label='Gradient', basex=2, linewidth=0.5)
    plt.legend(title='Solver')
    plt.grid('on')
    plt.xlim([min(steps), max(steps)])
    plt.xlabel('Function Evaluations')
    plt.ylabel('Absolute Error')
    plt.title('Solver Error vs. Evaluations')
    plt.show()


if __name__ == '__main__':
    # STILL NEEDED: Plots and gradient function
    check_functions()
    plot_functions()
