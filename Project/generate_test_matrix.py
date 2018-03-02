#!/usr/bin/env python
"""
Created on Mon Feb 26 16:23:21 2018

@author: cartemic
"""

import detonation as det
from random import random
import pandas as pd

# %% define functions


def User_input(user_query, desired_type):
    flag = True
    while flag:
        information = raw_input(user_query+' ').split()
        try:
            if desired_type is list:
                return information

            output = desired_type(*information)
            if isinstance(output, type(None)):
                raise ValueError
            else:
                return output
                flag = False
        except:
            print('Error: could not convert to ' + str(desired_type))
            print('Try again.\n')


def Output_results():
    pass


def Generate():
    # collect input from the user
    initial_pressure = User_input('Initial Pressure:', det.Pressure)
    initial_temperature = User_input('Initial Temperature:', det.Temperature)
    fuel = User_input('Fuel:', str)
    oxidizer = User_input('Oxidizer:', str)
    diluent_gases = User_input('Diluent gases (separated by spaces):', list)
    equivalence_ratios = User_input('Equivalence Ratios' +
                                    ' (separated by spaces):', list)
    dil_mass_fracs = User_input('Diluent mass fractions for diluted tests' +
                                ' (separated by spaces):', list)

    # initialize a detonation WON'T WORK YET
    my_detonation = det.Detonation(initial_pressure, initial_temperature, fuel, oxidizer)

# %% main program
# request test conditions from user
# build test matrix
# predict CJ velocity and estimate gas masses

if __name__ == '__main__':
    Generate()
