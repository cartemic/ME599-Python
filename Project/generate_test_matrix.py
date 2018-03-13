#!/usr/bin/env python
"""
Created on Mon Feb 26 16:23:21 2018

@author: cartemic
"""

import detonation as det
import numpy as np
import pandas as pd
import random
import itertools

# %% define functions


def add_row(self, row):
    # add a row to a pandas dataframe
    # https://stackoverflow.com/questions/10715965/
    # add-one-row-in-a-pandas-dataframe
    self.loc[len(self.index)] = row


pd.DataFrame.add_row = add_row


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


def Generate(initial_pressure,
             initial_temperature,
             fuel_string,
             oxidizer_string,
             diluent_str_list,
             equivalence_list,
             diluent_mf_list,
             replicates):

    initial_pressure = det.Pressure(initial_pressure)
    initial_temperature = det.Temperature(initial_temperature)

    # make sure there is an undiluted case
    if None not in diluent_str_list:
        diluent_str_list.append(None)
    diluent_str_list = sorted(diluent_str_list)

    # initialize a detonation
    my_detonation = det.Detonation(initial_pressure,
                                   initial_temperature,
                                   fuel_string,
                                   oxidizer_string)

    # list of colunm names for pandas dataframe
    column_titles = ['Diluent', 'Equivalence', 'Diluent MF',
                     'Fuel Pressure (psia)', 'Oxidizer Pressure (psia)',
                     'Diluent Pressure (psia)', 'CJ Speed (m/s)',
                     'Fuel Used (kg)', 'Oxidizer Used (kg)',
                     'Diluent Used (kg)']

    # empty list for storing dataframes
    df_list = []
    for replicate in xrange(replicates):
        print 'replicate', replicate
        # initialize blank list of test conditions
        df = pd.DataFrame(columns=column_titles)

        # block by diluent
        for i in xrange(len(diluent_str_list)):
            print 'diluent', i
            # build list of all test combinations
            test_conditions = list(itertools.product(*[equivalence_list,
                                                       [diluent_str_list[i]],
                                                       diluent_mf_list]))

            for j in xrange(len(test_conditions)):
                print 'test', j
                # select a random test condition
                [equivalence, diluent, mf] = test_conditions.pop(
                        random.randrange(len(test_conditions)))
                data = [diluent, equivalence, mf, [], [], [], [], [], [], []]
                # update detonation for each diluent, equivalence, and mf
                if diluent_str_list[i] is None:
                    # undiluted case
                    diluted = False
                    pass

                else:
                    # diluted case
                    my_detonation.set_equivalence(equivalence)
                    my_detonation.add_diluent(diluent, mf)
                    diluted = True
                # calculate partial pressures
                # calculate cj
                data[6] = my_detonation.CJ_Velocity(diluted).value
                # calculate mass used
                # put into sheet
                df.add_row(data)
        df_list.append(df)
    return df_list
# %% main program
# request test conditions from user
# build test matrix
# predict CJ velocity and estimate gas masses


if __name__ == '__main__':
    P0 = det.Pressure(1, 'atm')
    T0 = det.Temperature(70, 'F')
    fuel = 'H2'
    oxidizer = 'O2'
    diluents = ['N2', 'AR']
    equivalence = [0.75, 1.]
    diluent_mf = [0.1]
    test = Generate(P0, T0, fuel, oxidizer, diluents, equivalence, diluent_mf, 1)
