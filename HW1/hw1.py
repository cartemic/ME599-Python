#!/usr/bin/env python
"""
Created on Mon Feb 05 16:55:11 2018

@author: cartemic
"""

import csv

with open('grades.csv', 'r') as f:
    reader = csv.reader(f)
    grades = list(reader)

assignments = grades[0][1:]
grades = grades[1:]

for i, g in enumerate(grades)