#!/usr/bin/env python
"""
Created on Tue Feb 06 11:53:19 2018

@author: cartemic
"""

import sys
import os.path
import string


def comparison(my_file):
    """
    Opens a file and counts the number of total and unique words in it
    output: (# total words, # unique words, set of unique words)
    """
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
    return word_count, len(words), words


if len(sys.argv) < 3:
    # user has not given enough arguments
    print('Two arguments is the minimum requirement for a nutritious function')
elif len(sys.argv) > 3:
    # user has given too many arguments
    print('That\'s too many arguments! AUGH! MY PROCESSOR!')
else:
    # user has given the correct amount of arguments
    files = [sys.argv[1], sys.argv[2]]

    # ensure files actually exist and respond appropriately
    exist_1 = os.path.isfile(files[0])
    exist_2 = os.path.isfile(files[1])
    if exist_1 and exist_2:
        file_info = [comparison(f) for f in files]
        """
        file_info is a list of tuples:
            (total words, unique words, set of unique words)
        """

        for i, f in enumerate(files):
            print(f)
            print('    {0} words'.format(file_info[i][0]))
            print('    unique: {0}'.format(file_info[i][1]))

        # find out how many words are shared by the datasets
        shared = len(set.intersection(file_info[0][2], file_info[1][2]))

        for i, f in enumerate(files):
            print('Only {0:s}: {1}'.format(f, len(file_info[i][2]) - shared))

        print('Both files: {0}'.format(shared))
    elif not exist_1 and not exist_2:
        print('Both of your filenames are jacked up. Get it together!')
    elif not exist_1:
        print('Invalid first filename. Have you been drinking?')
    else:
        print('Invalid second filename. Try harder.')

"""
DEBUGGING CHECK:

test.txt
    9 words
    unique: 9
test2.txt
    19 words
    unique: 17
Only test.txt 1
Only test2.txt 9
Both files: 8


total wall time for war and peace and words comparison ~500-800ms << 10s :)
"""
