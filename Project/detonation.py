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
    pass


class Temperature():
    units = set(['K', 'C', 'F', 'R'])

    def __init__(self, temperature, unit='K'):
        """
        Try to treat input like a temperature. If this doesn't work, assign
        units, defaulting to Kelvin.
        """
        if unit not in Temperature.units:
            raise ValueError

        try:
            self.value = temperature.value
            self.unit = temperature.unit
        except:
            self.value = temperature
            self.unit = unit

    def to_Kelvin(self):
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
    # has a cj velocity and mass loss from tank estimate
    def __init__(self, Pressure, Temp, fuel, oxidizer, equivalence=1,
                 mechanism='gri30.cti'):
        self.mechanism = mechanism
        self.P = Pressure  # ADD UNIT FIXING
        try:
            self.T = Temp.to_Kelvin
        except:
            print('Bad temperature given, assuming units are Kelvin')
            self.T = Temperature(Temp)

        self.undiluted = ct.Solution(mechanism)
        self.undiluted.TP = (self.T.value, self.P)
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

        self.set_equivalence(equivalence)

    def set_equivalence(self, equivalence_ratio):
        # use Cantera to set equivalence ratio of undiluted mixture
        self.undiluted.set_equivalence_ratio(equivalence_ratio,
                                             self.fuel,
                                             self.oxidizer)

        # update equivalence ratio
        self.phi = equivalence_ratio
        if sum([self.undiluted.X > 0][0]) < 2:
            print('You can\t detonate that, ya dingus')
            return

    def get_mixture_string(self, diluted=False):
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
        # calculate and return CJ velocity
        [cj_speed, _] = sd.CJspeed(self.P.value, self.T.value,
                                   self.get_mixture_string(diluted),
                                   self.mechanism, 0)
        return Velocity(cj_speed)

    """
    ADD IN DILUTED CASE
    """

if __name__ == '__main__':
    T = Temperature(100)
