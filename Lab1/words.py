#!/usr/bin/env python
"""
Created on Tue Jan 16 12:51:36 2018

@author: Mick
"""

import string as st


def letter_count(input_string, letter_to_count):
    """
    Takes two string arguments: the first string is a bunch of text, and the
    second is a letter.  The function returns the number of occurrences of the
    letter in the text, and is case insensitive.
    """
    return(st.count(st.lower(input_string), st.lower(letter_to_count)))


if __name__ == "__main__":
    # test stuff
    test_string = 'woo woo AWOOGA'
    print(letter_count(test_string, 'w'))
    print(letter_count(test_string, 'z'))
