#!/usr/bin/env python
"""
Created on Mon Feb 05 16:55:11 2018

@author: cartemic
"""

import csv
import numpy as np


def assignment_scores(data, assignment_number):
    scores = np.array([])
    assignment_name = data[0][assignment_number]
    # collect scores from all students
    for i in xrange(len(data)-1):
        try:
            # add score to numpy array as a float rather than a string
            scores = np.append(scores,
                               float(data[i+1][assignment_number]))
        except ValueError:
            # get rid of those pesky 'EX' scores
            pass
    return assignment_name, scores


def hardest_assignment(data):
    num_assignments = len(data[0])-1
    assignments = dict()

    # organize assignments into a dictionary, removing any with all-zero scores
    for i in xrange(num_assignments):
        name, scores = assignment_scores(data, i+1)
        if max(scores) > 0:
            assignments[name] = np.mean(scores)

    # find and return hardest assignment
    return assignments.keys()[np.argmin(assignments.values)]


with open('grades.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

final_scores = assignment_scores(data, len(data[0])-1)[1]
final_avg = np.mean(final_scores)
final_med = np.median(final_scores)

print('Average Score: {0:.2f}'.format(final_avg))
print('Above Average: {0:.2f}%'.format(100 * sum(final_scores
                                                 >
                                                 final_avg
                                                 )/float(len(final_scores))))
print('Median Score: {0:.2f}'.format(final_med))
print('Above Median: {0:.2f}%'.format(
                                      100 * sum(final_scores
                                                >
                                                final_med
                                                )/float(len(final_scores))))
print('Hardest Assignment: ' + hardest_assignment(data))


#for i, g in enumerate(grades)