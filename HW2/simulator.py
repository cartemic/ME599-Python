#!/usr/bin/env python
"""
Created on Thu Mar 01 11:24:43 2018

@author: cartemic
"""

import subprocess
import random
import sys


def get_score(waypoint_file='waypoints', instance=0):
    return float(subprocess.check_output(['simulator',
                                          waypoint_file,
                                          str(instance)])
                 .split()[-1][:-1])


def generate_waypoints(use_basic=False):
    # add starting waypoint
    waypoints = [(-10, -10)]

    # add middle waypoints
    if use_basic:
        pass
    else:
        for i in range(10):
            waypoints.append((random.random()*10, random.random()*10))

    # add ending waypoint
    waypoints.append((10, 10))

    return waypoints


def output_waypoints(waypoints, file_name):
    # open file
    with open(file_name, 'w') as f:
        for i in xrange(len(waypoints)):
            f.write(str(waypoints[i][0]) + ' ' + str(waypoints[i][1]) + '\n')


def improve_waypoints(instance=0):
    # generate basic waypoint file
    basic_file = 'waypoints_basic'
    waypoints_basic = generate_waypoints(use_basic=True)
    output_waypoints(waypoints_basic, basic_file)
    basic_score = get_score(basic_file, instance)

    # generate improved waypoint file
    better_file = 'waypoints_better'
    waypoints_better = generate_waypoints()
    output_waypoints(waypoints_better, better_file)
    random_score = get_score(better_file, instance)
    if random_score < basic_score:
        print('boo')
        return(improve_waypoints(instance))

    return(basic_score, random_score)


if __name__ == '__main__':
    instance = 0
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            print('Too many arguments, using the first one')
        try:
            instance = int(sys.argv[1])
        except (TypeError, ValueError):
            print('Please input something numeric. Defaulting to 0.')

    print(improve_waypoints(instance))
