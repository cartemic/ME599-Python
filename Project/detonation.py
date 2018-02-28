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
    def __init__(self, Pressure, Temp, mixture, mechanism='gri30.cti'):
        pass


def CJ_Velocity(Pressure_Pa, Temp_K, mixture_string, mechanism='gri30.cti'):
    # ensure data types
    # check pressure, temperature units

    # calculate and return CJ velocity
    [cj_speed, _] = sd.CJspeed(Pressure_Pa, Temp_K, mixture_string,
                               mechanism, 0)
    return Velocity(cj_speed)


def Equivalence():
    pass


def Dilution():
    pass


if __name__ == '__main__':
    T = Temperature(100)
