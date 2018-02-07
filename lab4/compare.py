#!/usr/bin/env python
"""
Created on Tue Feb 06 11:53:19 2018

@author: cartemic
"""

import sys
import os.path
import string


def comparison(my_file):
    word_count = 0
    words = set()
    with open(my_file, 'r') as f:
        for line in f:
            line_words = line\
                          .strip()\
                          .lower()\
                          .translate(string.maketrans("", ""),
                                     string.punctuation)\
                          .split()
            [words.add(w) for w in line_words]
            word_count += len(line_words)
    return word_count, len(words)


def words_only_in(my_file):
    return None


def words_in_both(my_files):
    return None


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
        file_counts = [comparison(f) for f in files]
        for i, f in enumerate(files):
            print(f)
            print('    {0} words'.format(file_counts[i][0]))
            print('    unique: {0}'.format(file_counts[i][1]))

        for f in files:
            print('Only {0:s}: {1}'.format(f, words_only_in(f)))

#        print('Both files:',words_in_both(files))
    elif not exist_1 and not exist_2:
        print('Both of your filenames are jacked up.')
    elif not exist_1:
        print('Invalid first filename.')
    else:
        print('Invalid second filename.')
