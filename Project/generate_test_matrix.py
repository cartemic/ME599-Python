#!/usr/bin/env python
"""
Created on Mon Feb 26 16:23:21 2018

@author: cartemic
"""

import detonation as det
import pandas as pd
import random
import itertools
import os

# %% define functions


def add_row(self, row):
    # add a row to a pandas dataframe, code from
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


def Output_results(dataframe_list):
    for i, df in enumerate(dataframe_list):
        file_name = 'Test_matrix_replicate_' + str(i+1) + '.csv'
        if os.path.exists(file_name):
            os.remove(file_name)
        df.to_csv(file_name, index=False)


def Generate(initial_pressure,
             initial_temperature,
             fuel_string,
             oxidizer_string,
             diluent_str_list,
             equivalence_list,
             diluent_mf_list,
             tube_volume_m3,
             replicates):

    initial_pressure = det.Pressure(initial_pressure)
    initial_temperature = det.Temperature(initial_temperature)

    # make sure there is an undiluted case
    if 'None' not in diluent_str_list:
        # Insert at beginning of list. Uses a string because a NoneType causes
        # problems with the dataframe reordering later in the script.
        diluent_str_list.insert(0, 'None')

    # initialize a detonation
    my_detonation = det.Detonation(initial_pressure,
                                   initial_temperature,
                                   fuel_string,
                                   oxidizer_string)

    # list of colunm names for pandas dataframe
    column_titles = ['Diluent', 'Equivalence', 'Diluent MF',
                     'Fuel Pressure (Pa)', 'Oxidizer Pressure (Pa)',
                     'Diluent Pressure (Pa)', 'CJ Speed (m/s)',
                     'Fuel Used (kg)', 'Oxidizer Used (kg)',
                     'Diluent Used (kg)']

    # empty list for storing dataframes
    df_list = []
    for replicate in xrange(replicates):
        print 'replicate', replicate
        df = pd.DataFrame(columns=column_titles)
        # initialize blank list of test conditions
        if replicate == 0:
            # block by diluent USE MULTIPLE CORES
            for i in xrange(len(diluent_str_list)):
                print '    diluent', i
                # build list of all test combinations
                test_conditions = list(itertools.product(*[equivalence_list,
                                                         [diluent_str_list[i]],
                                                         diluent_mf_list]))

                for j in xrange(len(test_conditions)):
                    print '        test', j
                    # select a random test condition
                    [equivalence, diluent, mf] = test_conditions.pop(
                            random.randrange(len(test_conditions)))
                    data = [diluent, equivalence, mf,
                            [], [], [], [], [], [], []]

                    # update detonation for each diluent, equivalence, and mf
                    if diluent_str_list[i] is 'None':
                        # undiluted case
                        diluted = False
                        pass

                    else:
                        # diluted case
                        my_detonation.set_equivalence(equivalence)
                        my_detonation.add_diluent(diluent, mf)
                        diluted = True

                    # calculate partial pressures of each component. Filling
                    # will be done fuel -> oxidizer -> diluent, so partials
                    # will be added in this order in order to get cutoff
                    # pressures for each component.
                    pressures = my_detonation.get_pressures(diluted)
                    data[3] = pressures[fuel_string]
                    data[4] = data[3] + pressures[oxidizer_string]
                    try:
                        data[5] = data[4] + pressures[diluent_str_list[i]]
                    except:
                        data[5] = 'N/A'

                    # calculate cj
                    data[6] = my_detonation.CJ_Velocity(diluted).value
                    # calculate mass used
                    masses = my_detonation.get_mass(tube_volume_m3, diluted)
                    data[7] = masses[fuel_string]
                    data[8] = masses[oxidizer_string]
                    try:
                        data[9] = masses[diluent_str_list[i]]
                    except:
                        data[9] = 0.
                    # put into sheet
                    df.add_row(data)

        else:
            # randomize first dataframe
            # loop through blocked diluents
            for i, diluent in enumerate(diluent_str_list):
                # separate out current diluent
                sub_df = df_list[0][df_list[0].Diluent == diluent]

                # randomize this block and add it to the current dataframe
                new_order = [int(idx) for idx in sub_df.index]
                random.shuffle(new_order)
                df = pd.concat([df, sub_df.reindex(new_order)])

        # append current dataframe to list
        df_list.append(df)
    return df_list


# %% main program


if __name__ == '__main__':
    P0 = det.Pressure(1, 'atm')
    T0 = det.Temperature(70, 'F')
    tube_volume_m3 = 1.
    fuel = 'H2'
    oxidizer = 'O2'
    diluents = ['AR']
    equivalence = [0.75, 1., 1.25]
    diluent_mf = [0.1]
    replicates = 4
    test = Generate(P0, T0, fuel, oxidizer, diluents, equivalence, diluent_mf,
                    tube_volume_m3, replicates)
    Output_results(test)
