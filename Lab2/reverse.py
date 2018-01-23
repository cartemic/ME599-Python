#!/usr/bin/env python
"""
Created on Tue Jan 23 11:54:51 2018

@author: Mick
"""


def reverse_i(inputList):
    """
    Iteratively reverses a list
    """
    if inputList == []:
        return []
    else:
        theEnd = len(testList) - 1
        outputList = []
        for i in range(theEnd, -1, -1):
            outputList.append(inputList[i])

        return(outputList)


def reverse_r(inputList):
    """
    Recursively reverses a list
    """
    if inputList == []:
        return []
    else:
        location = len(inputList)-1
        outputList = inputList[:]
        if location == 0:
            return inputList
        else:
            outputList = [inputList[location]] +\
                          reverse_r(inputList[:location])
            return outputList


if __name__ == "__main__":
    """
    test stuff
    """

    testList = [1, None, 2., 'oop oop', True]

    print('original list')
    print('=============')
    print(testList)
    print('')

    print('iterative test')
    print('==============')
    print(reverse_i(testList))
    print(reverse_i([]))
    print('')

    print('recursive test')
    print('==============')
    print(reverse_r(testList))
    print(reverse_r([]))
