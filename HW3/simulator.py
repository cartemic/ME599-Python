#!/usr/bin/env python
"""
Created on Thu Mar 01 11:24:43 2018

@author: cartemic
"""

import subprocess
import os
from uuid import uuid4
import sys


class Simulator():
    def __init__(self, instance):
        self.instance = instance

    def evaluate(self, waypoints):
        filename = 'waypoints-' + str(uuid4())
#        filename = 'best-waypoints'

        # output waypoints
        with open(filename, 'w') as f:
            for i in xrange(len(waypoints)):
                f.write(str(waypoints[i][0]) +
                        ' ' +
                        str(waypoints[i][1]) +
                        '\n')

        # evaluate score
        score = float(subprocess.check_output(['simulator',
                                               filename,
                                               str(self.instance)]).
                      split()[-1][:-1])

        # remove file
        os.remove(filename)
        return score


if __name__ == '__main__':
    instance = 0
    num_points = 4
    basic_points = [[-10, -10], [10, 10]]
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            print('Too many arguments, using the first one')
        try:
            instance = int(sys.argv[1])
        except (TypeError, ValueError):
            print('Please input something numeric. Defaulting to 0.')

    test = Simulator(instance)
    print test.evaluate(basic_points)
