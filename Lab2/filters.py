#!/usr/bin/env python
"""
Created on Tue Jan 23 16:34:32 2018

@author: cartemic
"""

def mean_filter(inputList, filterWidth=3):
    """
    Accepts a list, and replaces each element (except the first and last) with
    the mean of itself and the elements before and after it. If the number of
    elements in the list is less than the filter width, this is not possible
    and the input list is returned unaltered.
    """
    filterWidth = int(filterWidth)
    numEl = len(inputList)
    if numEl < filterWidth:
        # yell at the fool who sent you such a short list
        print('That\'s too short of a list, bud.')
        return(inputList[:])
    else:
        outputList = []
        """
        NEVERMIND, IT'S OKAY TO HAVE LESS ELEMENTS PER INSTRUCTIONS
        for i in range(filterWidth/2):
            # start with unfiltered elements
            outputList.append(float(inputList[i]))
        """

        for i in range(filterWidth/2, numEl-filterWidth/2):
            # find the mean of each element and its surrounding elements
            theMean = sum(inputList[i-filterWidth/2:i+filterWidth/2+1]) /\
                      float(filterWidth)
            outputList.append(theMean)

        """
        NEVERMIND, IT'S OKAY TO HAVE LESS ELEMENTS PER INSTRUCTIONS
        for i in range(numEl-filterWidth/2, numEl):
            # finish with unfiltered elements
            outputList.append(float(inputList[i]))
        """

        return(outputList)
        
        
def median_filter(inputList, filterWidth=3):
    """
    Accepts a list, and replaces each element (except the first and last) with
    the median of itself and the elements before and after it. If the number of
    elements in the list is less than the filter width, this is not possible
    and the input list is returned unaltered.
    """
    filterWidth = int(filterWidth)
    numEl = len(inputList)
    if numEl < filterWidth:
        # yell at the fool who sent you such a short list
        print('That\'s too short of a list, bud.')
        return(inputList[:])
    else:
        outputList = []
        """
        NEVERMIND, IT'S OKAY TO HAVE LESS ELEMENTS PER INSTRUCTIONS
        for i in range(filterWidth/2):
            # start with unfiltered elements
            outputList.append(inputList[i])
        """

        for i in range(filterWidth/2, numEl-filterWidth/2):
            # find the median of each element and its surrounding elements
            surroundings = inputList[i-filterWidth/2:i+filterWidth/2+1]
            surroundings.sort()
            theMedian = surroundings[1]
            outputList.append(theMedian)

        """
        NEVERMIND, IT'S OKAY TO HAVE LESS ELEMENTS PER INSTRUCTIONS
        for i in range(numEl-filterWidth/2, numEl):
            # finish with unfiltered elements
            outputList.append(inputList[i])
        """

        return(outputList)


if __name__ == "__main__":
    """
    test stuff
    """
    testList = [1, 42, 2.01, 33, 7.25, 16, 123]
    print(testList)
    print('')

    print('test mean filter')
    print('==================')
    print(mean_filter(testList))
    print(mean_filter(testList, 5))
    print(mean_filter([17, 2]))
    print(mean_filter([]))
    print('')

    print('test median filter')
    print('==================')
    print(median_filter(testList))
    print(median_filter(testList, 5))
    print(median_filter([17, 2]))
    print(median_filter([]))
