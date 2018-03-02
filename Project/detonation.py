#!/usr/bin/env python
"""
Created on Mon Feb 26 16:23:21 2018

@author: cartemic
"""

import SDToolbox as sd
import cantera as ct


class Velocity():
    pass


class Pressure():
    units = set(['Pa', 'kPa', 'psia', 'atm'])

    def __init__(self, pressure, unit='Pa'):
        '''
        A pressure object for easy unit conversion to prevent the user from
        being too dumb. Units default to Pascals if not specified.
        '''
        # make sure units are good
        if unit not in Pressure.units:
            raise ValueError

        # duck type it for ease of use
        try:
            self.value = pressure.value
            self.unit = pressure.unit
        except:
            self.value = pressure
            self.unit = unit

    def to_Pa(self):
        '''
        Converts a pressure object to Pa
        '''
        if self.unit == 'Pa':
            return self
        elif self.unit == 'kPa':
            return Pressure(self.value * 1000.)
        elif self.unit == 'psia':
            return Pressure(self.value / 0.00014503773800722)
        else:
            return Pressure(self.value * 101325)

    def __str__(self):
        return str(self.value) + ' ' + self.unit

    def __repr__(self):
        return str(self)


class Temperature():
    units = set(['K', 'C', 'F', 'R'])

    def __init__(self, temperature, unit='K'):
        '''
        A temperature object for easy unit conversion to prevent the user from
        being too dumb. Units default to Kelvin if not specified.
        '''
        # make sure units are good
        if unit not in Temperature.units:
            raise ValueError

        # duck type it for ease of use
        try:
            self.value = temperature.value
            self.unit = temperature.unit
        except:
            self.value = temperature
            self.unit = unit

    def to_Kelvin(self):
        '''
        Converts a temperature object to Kelvin
        '''
        if self.unit == 'K':
            return self
        elif self.unit == 'C':
            return Temperature(self.value + 273.15)
        elif self.unit == 'F':
            return Temperature((self.value - 32.) * 5./9., 'C').to_Kelvin()
        else:
            return Temperature(self.value - 459.67, 'F').to_Kelvin()

    def __str__(self):
        return str(self.value) + ' ' + self.unit

    def __repr__(self):
        return str(self)


class Detonation():
    '''
    Docstring goes here
    '''
    # has a cj velocity and mass loss from tank estimate
    def __init__(self, init_pressure, init_temp, fuel, oxidizer, equivalence=1,
                 mechanism='gri30.cti'):
        # define chemical mechanism for cantera and sdtoolbox
        self.mechanism = mechanism

        # ensure good pressure input
        try:
            self.P = init_pressure.to_Pa()
        except:
            print('Bad pressure given, assuming units are Pascals')
            self.P = Pressure(init_pressure)

        # ensure good temperature input
        try:
            self.T = init_temp.to_Kelvin
        except:
            print('Bad temperature given, assuming units are Kelvin')
            self.T = Temperature(init_temp)

        # initialize undiluted gas solution in Cantera
        self.undiluted = ct.Solution(mechanism)
        self.undiluted.TP = (self.T.value, self.P)

        # make sure the user input species that are in the mechanism file
        good_species = self.undiluted.species_names
        if fuel in good_species:
            self.fuel = fuel
        else:
            print('Bad Fuel')
            return
        if oxidizer in good_species:
            self.oxidizer = oxidizer
        else:
            print('Bad Oxidizer')
            return

        # set the default equivalence ratio
        self.set_equivalence(equivalence)

    def set_equivalence(self, equivalence_ratio):
        '''
        Sets the equivalence ratio of the undiluted mixture using Cantera
        '''
        # set the equivalence ratio
        self.undiluted.set_equivalence_ratio(equivalence_ratio,
                                             self.fuel,
                                             self.oxidizer)

        # ensure good inputs were given and record new equivalence ratio
        if sum([self.undiluted.X > 0][0]) < 2:
            print('You can\t detonate that, ya dingus')
            return
        self.phi = equivalence_ratio

    def get_mixture_string(self, diluted=False):
        '''
        Gets a mixture string from either the diluted or undiluted Cantera
        solution object, which is then used to calculate CJ velocity using
        SDToolbox
        '''
        if diluted:
            cantera_solution = self.diluted
        else:
            cantera_solution = self.undiluted
        mixture_list = []
        for i, species in enumerate(cantera_solution.species_names):
            if cantera_solution.X[i] > 0:
                mixture_list.append(species + ':' +
                                    str(cantera_solution.X[i]))
        return ' '.join(mixture_list)

    def CJ_Velocity(self, diluted=False):
        '''
        Calculates CJ velocity using SDToolbox
        '''
        [cj_speed, _] = sd.CJspeed(self.P.value, self.T.value,
                                   self.get_mixture_string(diluted),
                                   self.mechanism, 0)
        return Velocity(cj_speed)

    """
    ADD IN DILUTED CASE
    """

if __name__ == '__main__':
    T = Temperature(100)
