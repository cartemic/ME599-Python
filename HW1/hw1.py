#!/usr/bin/env python
"""
Created on Mon Feb 05 16:55:11 2018

@author: cartemic
"""

from __future__ import print_function
import pandas as pd


def count_grades(percentage_list, grade_scheme):
    # initialize blank dictionary for grade counts
    grades = dict([letter, 0] for letter in grade_scheme.keys())
    whiners = 0

    for score in percentage_list:
        for loc, max_min in enumerate(grade_scheme.values()):
            if (score < max_min[0]) and (score >= max_min[1]):
                grades[grade_scheme.keys()[loc]] += 1
                if max_min[0] < 100. and max_min[0] - score < 0.5:
                    whiners += 1

    return grades, whiners


def new_grades(percentage_list, grade_scheme):
    grades = dict([letter, 0] for letter in grade_scheme.keys())
    for grade in grade_scheme.keys():
        for i in xrange(grade_scheme[grade]):
            grades[grade] += 1
    grades['F'] = len(percentage_list) - sum(grades.values())
    return grades


# get some data
data = pd.read_csv('grades.csv', sep=',').apply(pd.to_numeric, errors='coerce')

# calculate assignment percentages
scores = data.mean()/data.max()

# separate out lab scores
lab_scores = data.iloc[:, ['lab ' in data.keys()[k].lower()
                       for k in xrange(len(data.keys()))]]
lab_scores = 100 * lab_scores.mean() / lab_scores.max()

# calculate average, median, and related student percentages
final_grades = 100 * data.iloc[:, -1] / data.max()[-1]
final_avg = final_grades.mean()
above_avg = 100*sum(data.iloc[:, -1] > data.iloc[:, -1].mean())/data.max()[0]
final_med = 100*data.median()[-1]/data.max()[-1]
above_med = 100*sum(data.iloc[:, -1] > data.iloc[:, -1].median())/data.max()[0]

# find the hardest assignment and lab
hardest_assign = scores[scores == scores.min()].keys()[0]
hardest_lab = lab_scores[lab_scores == lab_scores.min()].keys()[0]

# define normal grading limits
normal_grade_scheme = {'A': [100.1, 94., 0],
                       'A-': [94., 90., 1],
                       'B+': [90., 87., 2],
                       'B': [87., 84., 3],
                       'B-': [84., 80., 4],
                       'C+': [80., 77., 5],
                       'C': [77., 74., 6],
                       'C-': [74., 70., 7],
                       'D+': [70., 67., 8],
                       'D': [67., 64., 9],
                       'D-': [64., 61., 10],
                       'F': [61., 0., 11]}

# define modified grading limits
num_students = len(data)
new_grade_scheme = {'A': int(num_students * 0.1),
                    'B': int(num_students * 0.2),
                    'C': int(num_students * 0.3),
                    'D': int(num_students * 0.3)}

# calculate grades
grades, whiners = count_grades(final_grades.values, normal_grade_scheme)
new_grades = new_grades(final_grades.values, new_grade_scheme)

# print statistics
print('Average Score:      {0:.2f}'.format(final_avg))
print('Above Average:      {0:.2f}%'.format(above_avg))
print('Median Score:       {0:.2f}'.format(final_med))
print('Above Median:       {0:.2f}%'.format(above_med))

# print hardest things
print()
print('Hardest Assignment: ' + hardest_assign)
print('Hardest Lab:        ' + hardest_lab)

# properly sort and print grade counts using usual grading scheme
print()
print('Usual grading scheme:')
[print('{0:2s}: {1:6.0f}'.format(grade, grades[grade]))
 for (grade, grade_range) in sorted(normal_grade_scheme.items(),
                                    key=lambda (grade,
                                                grade_range): grade_range,
                                    reverse=True)]

# prepare the floodgates
print()
print('{0} students will complain about their grade'.format(whiners))

# properly sort and print grade counts using new grade scheme
print()
print('New grading scheme:')
[print('{0:2s}: {1:6.0f}'.format(grade, new_grades[grade]))
 for (grade, grade_range) in sorted(new_grades.items())]
