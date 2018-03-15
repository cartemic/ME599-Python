#!/usr/bin/env python
"""
Created on Wed Mar 14 11:13:19 2018

@author: cartemic
"""
import itertools
import random
import detonation as det


def first_replicate(initial_pressure,
                    initial_temperature,
                    fuel_string,
                    oxidizer_string,
                    equivalence_list,
                    current_diluent,
                    diluent_mf_list,
                    tube_volume_m3,
                    df,
                    call_number,
                    mp_out):

    # initialize a detonation
    my_detonation = det.Detonation(initial_pressure,
                                   initial_temperature,
                                   fuel_string,
                                   oxidizer_string)

    # build list of all test combinations
    test_conditions = list(itertools.product(*[equivalence_list,
                                             [current_diluent],
                                             diluent_mf_list]))

    for j in xrange(len(test_conditions)):
        # select a random test condition
        [equivalence, diluent, mf] = test_conditions.pop(
                random.randrange(len(test_conditions)))
        data = [diluent, equivalence, mf,
                [], [], [], [], [], [], []]

        # update detonation for each diluent, equivalence, and mf
        if current_diluent is 'None':
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
            data[5] = data[4] + pressures[current_diluent]
        except:
            data[5] = 'N/A'

        # calculate cj
        data[6] = my_detonation.CJ_Velocity(diluted).value
        # calculate mass used
        masses = my_detonation.get_mass(tube_volume_m3, diluted)
        data[7] = masses[fuel_string]
        data[8] = masses[oxidizer_string]
        try:
            data[9] = masses[current_diluent]
        except:
            data[9] = 0.
        # put into sheet
        df.add_row(data)
    mp_out.put_nowait((call_number, df))
