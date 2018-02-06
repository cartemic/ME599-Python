#!/usr/bin/env python
"""
Created on Tue Feb 06 11:53:19 2018

@author: cartemic
"""

import sys
import os.path
import string


def total_words(my_file):
    with open(my_file, 'r') as f:
        word_count = 0
        for line in f:
            word_count += len(line
                              .strip()
                              .lower()
                              .translate(None, string.punctuation)
                              .split())
            print(word_count)
            print(line)


total_words('test.txt')


def unique_words(my_file):
    return 1


def words_only_in(my_file):
    return 2


def words_in_both(my_files):
    return 3


if len(sys.argv) < 3:
    # user has not given enough arguments
    print('Two arguments is the minimum requirement for a nutritious function')
elif len(sys.argv) > 3:
    # user has given too many arguments
    print('I\'m ignoring everything but your first two arguments')
else:
    # user has given the correct amount of arguments
    files = [sys.argv[1], sys.argv[2]]

    # ensure files actually exist and respond appropriately
    exist_1 = os.path.isfile(files[0])
    exist_2 = os.path.isfile(files[1])
    if exist_1 and exist_2:
        for f in files:
            print(f)
            print('    {0} words'.format(total_words(f)))
            print('    unique: {0}'.format(unique_words(f)))

        for f in files:
            print('Only {0:s}: {1}'.format(f, words_only_in(f)))

        print('Both files:',words_in_both(files))
    elif not exist_1 and not exist_2:
        print('Both of your filenames are jacked up.')
    elif not exist_1:
        print('Invalid first filename.')
    else:
        print('Invalid second filename.')