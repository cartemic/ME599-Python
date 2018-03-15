#!/usr/bin/env python
"""
Created on Thu Mar 01 11:24:43 2018

@author: cartemic
"""

import subprocess
import random
import sys
import multiprocessing as mp
import os


def get_score(waypoint_file='waypoints', instance=0):
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    return float(subprocess.check_output(['simulator',
                                          waypoint_file,
                                          str(instance)], startupinfo=si)
                 .split()[-1][:-1])


def generate_waypoints(num_points=10, use_basic=False):
    # add starting waypoint
    waypoints = [(-10, -10)]
    num_points = int(num_points)

    # add middle waypoints
    if use_basic:
        pass
    else:
        for i in range(num_points-2):
            waypoints.append((random.random()*20-10., random.random()*20-10))

    # add ending waypoint
    waypoints.append((10, 10))

    return waypoints


def get_new_point(point, point_step):
    decider = random.random()
    if decider < 0.5:
        sign = 1
    else:
        sign = -1

    scale = 1 + sign * random.random() * 0.2
    point = point * scale + sign * point_step
    if point < -10:
        point = -10
    elif point > 10:
        point = 10
    return point


def refine_waypoints(waypoints_list, point_step, instance, core_num,
                     score_limit=1e6, run_limit=100):
    # safe input waypoint file and generates score
    file_name = 'waypoints_input'+str(core_num)
    output_waypoints(waypoints_list, file_name)
    score = get_score(file_name, instance)
    os.remove(file_name)

    # start improving
    num_points = len(waypoints_list)
    waypoints_current = sorted(waypoints_list)
    count = 0
    while score <= score_limit:
        count += 1
        for i in range(1, num_points-1):
            file_name = 'waypoints_test'+str(core_num)
            [x, y] = waypoints_current[i]

            # change value of current x, y plus/minus step
            new_points = [[x, y],
                          [get_new_point(x, point_step),
                           get_new_point(y, point_step)]]
            waypoints_test = waypoints_current[:]
            waypoints_test[i] = new_points[1]
            output_waypoints(waypoints_test, file_name)
            new_scores = [score, get_score(file_name, instance)]

            # evaluate each change and keep best improvement
            waypoints_current[i] = new_points[new_scores
                                              .index(max(new_scores))]
            score = max(new_scores)
        if count == run_limit:
                break


def output_waypoints(waypoints, file_name):
    # open file and write
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
    num_points = 20
    point_step = 0.1
    instance = 0
    score_limit = 1e7
    num_runs = 100
    multiple_cores = True
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            print('Too many arguments, using the first one')
        try:
            instance = int(sys.argv[1])
        except (TypeError, ValueError):
            print('Please input something numeric. Defaulting to 0.')

    if multiple_cores:
        cores = mp.cpu_count()
        processes = []
        scores = []
        print 'starting multi-core tests on', cores, 'cores'
        print 'running...',
        for core in xrange(cores):
            processes.append(mp.Process(target=refine_waypoints,
                                        args=(generate_waypoints(num_points),
                                              point_step,
                                              instance,
                                              core,
                                              score_limit,
                                              num_runs)))
            processes[-1].start()
        for p in processes:
            p.join()

        score = 0
        for i in xrange(cores):
            current_file = 'waypoints_test'+str(i)
            new_score = get_score(current_file)
            if new_score > score:
                score = new_score
                if os.path.isfile('waypoints'):
                    os.remove('waypoints')
                os.rename(current_file, 'waypoints')
            else:
                os.remove(current_file)

    else:
        refine_waypoints(generate_waypoints(num_points), point_step,
                         instance, 0)
        score = get_score('waypoints_test0')
        if os.path.isfile('waypoints'):
            os.remove('waypoints')
        os.rename('waypoints_test0', 'waypoints')

    print 'DONE!'
    print 'HIGH SCORE:', score
