#!/usr/bin/env python
"""
Created on Thu Mar 15 10:15:13 2018

@author: cartemic
"""

import copy
import inspect


class wingus():
    def do_stuff(self, thing1, thing2, thing3):
        print thing1, thing2, thing3


def intercept(f):
    # make a copy of the class
    newf = copy.deepcopy(f)

    # collect built-in functions
    builtin_functions = [function for function in dir(newf)
                         if '__' in function]

    # collect custom functions
    custom_functions = [function for function in dir(newf)
                        if '__' not in function]

    # collect arguments
    mean_args = inspect.getargspec(getattr(newf, custom_functions[0]))[0][1:]

    # do mean things and then make it look like you didn't
    def mean_function(f, *mean_args):
        lists = [item for item in mean_args]
        new_func = custom_functions[0] + '0'
        exec('f.{0}(*lists)'.format(new_func)) in locals()

    # replace original function with mean function, and move original to a
    # new location so it can still be called by mean function
    move_func = eval('f.{0}'.format(custom_functions[0]))
    setattr(f, custom_functions[0]+'0', move_func)
    setattr(f, custom_functions[0], mean_function)


intercept(wingus)
test = wingus()
test.do_stuff(1, 2, 3)
