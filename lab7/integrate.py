#!/usr/bin/env python
"""
Created on Tue Feb 27 15:51:21 2018

@author: cartemic
"""

import numpy as np
import random
from matplotlib import pyplot as plt


plt.close('all')


def integrate(f, a, b, intervals=100):
    integrate.__name__ = 'Riemann'

    try:
        if b <= a:
            print('Bad bounds! You fool!')
            raise ValueError
        elif intervals <= 0:
            print('Bogus number of intervals! Argh!')
            raise ValueError

        integral = 0.
        delta = (float(b) - float(a))/(float(intervals) - 1)

        for x in np.linspace(a, b, intervals):
            integral += delta * f(x)

        return integral

    except:
        print('ERROR: ' + integrate.__name__)
        print('You gave me bad inputs!')
        return None


def integrate_mc(f, a, b, bounds=None, samples=1000):
    try:
        integrate_mc.__name__ = 'Monte Carlo'
        a = float(a)
        b = float(b)
        try:
            (c, d) = bounds
            c = float(c)
            d = float(d)
        except:
            c = 0
            d = 0

        if b <= a:
            print('Bad bounds! You fool!')
            raise ValueError
        elif d <= c:
            print('Bad c, d pair. Good thing I don\'t use those.')
        elif samples <= 0:
            print('Bogus number of samples! Argh!')
            raise ValueError

        '''
        the method from the class notes does not work. This method is from the
        Wikipedia page linked in the assignment. c and d are unused.
        '''

        # evaluate function
        integral = 0.
        for i in xrange(samples):
            x = random.random() * (b - a) + a
            integral += f(x)
        return (b - a) / (samples - 1) * integral

    except:
        print('ERROR: ' + integrate_mc.__name__)
        print('You gave me bad inputs!')
        return None


def parabola(x):
    return x**2


def sin(x):
    return np.sin(x)


def tester_riemann(start, end, steps):
    end = float(end)
    start = float(start)
    analytical = [end**3/3 - start**3/3, np.cos(start) - np.cos(end)]
    test_funcs = [parabola, sin]
    test = [integrate(f, start, end, steps) for f in test_funcs]
    for i in xrange(len(test)):
        error = np.abs(analytical[i]-test[i])/analytical[i]
        print(test_funcs[i].__name__)
        print('integrated: {0:1.4e}'.format(test[i]))
        print('analytical: {0:1.4e}'.format(analytical[i]))
        print('error %:    {0:1.4e}'.format(error))
        print


def tester_mc(start, end, bc, steps):
    end = float(end)
    start = float(start)
    analytical = [end**3/3 - start**3/3, np.cos(start) - np.cos(end)]
    test_funcs = [parabola, sin]
    test = [integrate_mc(f, start, end, bc, steps) for f in test_funcs]
    for i in xrange(len(test)):
        error = np.abs(analytical[i]-test[i])/analytical[i]
        print(test_funcs[i].__name__)
        print('integrated: {0:1.4e}'.format(test[i]))
        print('analytical: {0:1.4e}'.format(analytical[i]))
        print('error %:    {0:1.4e}'.format(error))
        print


def plot_results(start, end):
    functions = [integrate, integrate_mc]
    int_args = [[parabola, start, end, None],
                [parabola, start, end, (0, 1), None]]
    steps = np.power(2, np.array(range(6, 21)))
    analytical = end**3/3 - start**3/3
    for i, integrator in enumerate(functions):
        error = []
        for s in steps:
            int_args[i][-1] = s
            numerical = integrator(*tuple(int_args[i]))
            error.append(abs(analytical - numerical))
        plt.semilogx(steps, error, label=integrator.__name__, basex=2)
        plt.legend()
        plt.xlabel('Intervals/Samples')
        plt.ylabel('Absolute Error')
        plt.title('Absolute Error of Riemann and Monte-Carlo Integrators')
        plt.grid('on')
        plt.xlim([min(steps), max(steps)])
    plt.show()


def approximate_pi(number_samples):
    try:
        number_samples = int(number_samples)
        if number_samples <= 0:
            raise ValueError
    except:
        print('Bogus sample number')
        return None

    success = 0.
    for i in range(number_samples):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            success += 1

    return 4. * success / number_samples


if __name__ == '__main__':
    # enter test parameters
    start = 0.
    stop = 5.
    steps = 1000
    error_limit = 0.005

    # test riemann integrator using a parabola and sinusoid
    print('RIEMANN')
    print('=======')
    tester_riemann(start, stop, steps)
    print

    # test monte carlo integrator using a parabola and sinusoid
    print('MONTE CARLO')
    print('===========')
    tester_mc(start, stop, (0, 1), steps)

    plot_results(0, 5)
