#!/usr/bin/env python
"""
Created on Mon Feb 05 16:55:11 2018

@author: cartemic
"""

import numpy as np
import pandas as pd


data = pd.read_csv('grades.csv', sep=',').apply(pd.to_numeric, errors='coerce')

scores = data.mean()/data.max()
final_avg = 100*data.mean()[-1]/data.max()[-1]
above_avg = 100*sum(data.iloc[:,-1] > data.iloc[:,-1].mean())/data.max()[0]
final_med = 100*data.median()[-1]/data.max()[-1]
above_med = 100*sum(data.iloc[:,-1] > data.iloc[:,-1].median())/data.max()[0]
lowest_assign = scores[scores == scores.min()].keys()[0]

print('Average Score:      {0:.2f}'.format(final_avg))
print('Correct:            49.75\n')
print('Above Average:      {0:.2f}%'.format(above_avg))
print('Correct:            60.37%\n')
print('Median Score:       {0:.2f}'.format(final_med))
print('Correct:            68.93\n')
print('Above Median:       {0:.2f}%'.format(above_med))
print('Correct:            50.00%\n')
print('Hardest Assignment: ' + lowest_assign)
print('Correct:            ' + 'Midterm II (ECampus) (7083673)\n')
