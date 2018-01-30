#!/usr/bin/env python
"""
Created on Tue Jan 23 08:00:44 2018

@author: Mick
"""


def sum_i(numberList):
    """
    Takes a list of numbers as its argument, and returns the sum of all the
    numbers in the list using a for loop
    """

    theSum = 0
    for num in numberList:
        theSum = theSum + num
    return theSum


def sum_r(numberList):
    """
    Takes a list of numbers as its argument, and returns the sum of all the
    numbers in the list recursively
    """
    if len(numberList) > 1:
        return(numberList[0] + sum_r(numberList[1:]))
    elif len(numberList) == 0:
        return 0
    else:
        return numberList[0]


if __name__ == "__main__":
    """
    test stuff
    """

    listInts = [1, 1, 3]
    listFloats = [1., 1., 3.]
    listMixed = [1., 1, 3]

    print('built in')
    print('========')
    print('ints:   {0}'.format(sum(listInts)))
    print('floats: {0}'.format(sum(listFloats)))
    print('mixed:  {0}'.format(sum(listMixed)))
    print('mixed:  {0}'.format(sum([])))
    print('')

    print('test sum_i()')
    print('============')
    print('ints:   {0}'.format(sum_i(listInts)))
    print('floats: {0}'.format(sum_i(listFloats)))
    print('mixed:  {0}'.format(sum_i(listMixed)))
    print('mixed:  {0}'.format(sum_i([])))
    print('')

    print('test sum_r()')
    print('============')
    print('ints:   {0}'.format(sum_r(listInts)))
    print('floats: {0}'.format(sum_r(listFloats)))
    print('mixed:  {0}'.format(sum_r(listMixed)))
    print('mixed:  {0}'.format(sum_r([])))
    print('')
