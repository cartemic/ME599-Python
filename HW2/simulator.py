#!/usr/bin/env python
"""
Created on Thu Mar 01 11:24:43 2018

@author: cartemic
"""

import subprocess
import random
import sys
import os


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
        for i in range(1):
            waypoints.append((random.random()*20-10., random.random()*20-10))

    # add ending waypoint
    waypoints.append((10, 10))

    return sorted(waypoints)


def output_waypoints(waypoints, file_name):
    # open file and write
    with open(file_name, 'w') as f:
        for i in xrange(len(waypoints)):
            f.write(str(waypoints[i][0]) + ' ' + str(waypoints[i][1]) + '\n')


def improve_waypoints(waypoint_step=0.1, instance=0):
    # generate basic waypoint file
    basic_file = 'basic_waypoints'
    better_file = 'better_waypoints'
    if os.path.exists(better_file):
        os.remove(better_file)
    waypoints_basic = generate_waypoints(use_basic=True)
    waypoints_better = generate_waypoints()
    output_waypoints(waypoints_basic, basic_file)
    output_waypoints(waypoints_better, better_file)
    basic_score = get_score(basic_file, instance)
    better_score = get_score(better_file)
#    new_score = [better_score, better_score]
#    num_waypoints = len(waypoints_better)
    count = 0
#    repeat_count = 0

    # generate improved waypoint file
    while better_score >= basic_score:
        count += 1
        print 'Attempt', count
        waypoints_better = generate_waypoints()
        output_waypoints(waypoints_better, better_file)
        better_score = get_score(better_file, instance)
# dumpster fire attempt at extended pattern search
# which finds a local optimum because it is a dick
#        improvement_indices = range(1, num_waypoints-2)
#        for i in improvement_indices[:]:
#            # generate index for improvement and removal
#            random_index = random.randrange(len(improvement_indices))
#            print 'improving point', random_index
#            print improvement_indices
#
#            # improve the score using the point at random_index
#            [x, y] = waypoints_better[improvement_indices[random_index]]
#
#            # move the points
#            for direction in range(4):
#                if direction == 0:
#                    # go right
#                    x = min(x + waypoint_step, 10)
#                elif direction == 1:
#                    # go down
#                    y = max(y - waypoint_step, -10)
#                elif direction == 2:
#                    # go left
#                    x = max(x - waypoint_step, -10)
#                else:
#                    # go up
#                    y = min(y + waypoint_step, 10)
#
#                # replace current point with moved point
#                waypoints_better[improvement_indices[random_index]] = (x, y)
#
#                # check for score improvement
#                output_waypoints(waypoints_better, better_file)
#                new_score[0] = get_score(better_file, instance)
#                print '    old score:', new_score[1]
#                print '    new score:', new_score[0]
#                if new_score[0] < new_score[1]:
#                    print '    SUCCESS!'
#                    break
#            # remove this point
#            print improvement_indices.pop(random_index)
#
#            # cut step down if no improvement over last two runs
#            if new_score[0] == new_score[1]:
#                repeat_count += 1
#            else:
#                new_score[1] = new_score[0]
#
#            if repeat_count == 2:
#                repeat_count = 0
#                waypoint_step /= 2.
#
#        better_score = new_score[0]

    return(basic_score, better_score)


if __name__ == '__main__':
    instance = 0
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            print('Too many arguments, using the first one')
        try:
            instance = int(sys.argv[1])
        except (TypeError, ValueError):
            print('Please input something numeric. Defaulting to 0.')

    waypoint_step = 2.
    scores = improve_waypoints(waypoint_step, instance)
    print('SUCCESS!\n\nold score: {0}      new score: {1}'
          .format(scores[0], scores[1]))
