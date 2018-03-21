#!/usr/bin/env python
"""
Created on Mon Feb 26 16:23:21 2018

@author: cartemic
"""

import SDToolbox as sd
import cantera as ct


class Velocity():
    '''
    A velocity object for easy unit envforcement to prevent the user from
    being too dumb. The only units here are m/s because I have no reason to
    use other units in this application. They can be added later if needed.
    '''
    units = set(['m/s'])

    def __init__(self, velocity, unit=None):
        # duck type it for ease of use
        try:
            self.value = velocity.value
            self.unit = velocity.unit
        except AttributeError:
            try:
                if unit is None:
                    unit = 'm/s'
                    print('No unit given. Assuming ' + unit)
                elif unit not in Velocity.units:
                    raise ValueError
                self.value = float(velocity)
                self.unit = unit
            except ValueError:
                print('Bogus velocity input')
                raise ValueError

    def __str__(self):
        return str(self.value) + ' ' + self.unit

    def __repr__(self):
        return str(self)


class Pressure():
    '''
    A pressure object for easy unit conversion to prevent the user from
    being too dumb. Units default to Pascals if not specified.
    '''
    units = set(['Pa', 'kPa', 'psia', 'atm'])

    def __init__(self, pressure, unit=None):
        # duck type it for ease of use
        try:
            self.value = pressure.value
            self.unit = pressure.unit
        except AttributeError:
            try:
                if unit is None:
                    unit = 'Pa'
                    print('No unit given. Assuming ' + unit)
                elif unit not in Pressure.units:
                    raise ValueError
                self.value = float(pressure)
                self.unit = unit
            except ValueError:
                print('Bogus pressure input')
                raise ValueError

    def to_Pa(self):
        '''
        Converts a pressure object to Pa
        '''
        if self.unit == 'Pa':
            return self
        elif self.unit == 'kPa':
            return Pressure(self.value * 1000., 'Pa')
        elif self.unit == 'psia':
            return Pressure(self.value / 0.00014503773800722, 'Pa')
        else:
            return Pressure(self.value * 101325, 'Pa')

    def __str__(self):
        return str(self.value) + ' ' + self.unit

    def __repr__(self):
        return str(self)

    def __mul__(self, other):
        return Pressure(other * self.value, self.unit)

    def __rmul__(self, other):
        return self * other


class Temperature():
    '''
    A temperature object for easy unit conversion to prevent the user from
    being too dumb. Units default to Kelvin if not specified.
    '''
    units = set(['K', 'C', 'F', 'R'])

    def __init__(self, temperature, unit=None):
        # duck type it for ease of use
        try:
            self.value = temperature.value
            self.unit = temperature.unit
        except AttributeError:
            try:
                if unit is None:
                    unit = 'K'
                    print('No unit given. Assuming ' + unit)
                elif unit not in Temperature.units:
                    raise ValueError
                self.value = float(temperature)
                self.unit = unit
            except ValueError:
                print('Bogus temperature input')
                raise ValueError

    def to_Kelvin(self):
        '''
        Converts a temperature object to Kelvin
        '''
        if self.unit == 'K':
            return self
        elif self.unit == 'C':
            return Temperature(self.value + 273.15, 'K')
        elif self.unit == 'F':
            return Temperature((self.value - 32.) * 5./9., 'C').to_Kelvin()
        else:
            return Temperature(self.value - 459.67, 'F').to_Kelvin()

    def __str__(self):
        return str(self.value) + ' ' + self.unit

    def __repr__(self):
        return str(self)

    def __mul__(self, other):
        return Temperature(other * self.value, self.unit)

    def __rmul__(self, other):
        return self * other


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
        except AttributeError:
            print('Bad pressure given, assuming units are Pascals')
            self.P = Pressure(init_pressure, 'Pa')

        # ensure good temperature input
        try:
            self.T = init_temp.to_Kelvin()
        except AttributeError:
            print('Bad temperature given, assuming units are Kelvin')
            self.T = Temperature(init_temp, 'K')

        # initialize undiluted gas solution in Cantera
        self.undiluted = ct.Solution(mechanism)
        self.undiluted.TP = (self.T.value, self.P.value)

        # make sure the user input species that are in the mechanism file
        good_species = self.undiluted.species_names
        if fuel in good_species:
            self.fuel = fuel
        else:
            print('Bad Fuel')
            raise ValueError
        if oxidizer in good_species:
            self.oxidizer = oxidizer
        else:
            print('Bad Oxidizer')
            raise ValueError

        # set the default equivalence ratio
        self.set_equivalence(equivalence)

    def set_equivalence(self, equivalence_ratio):
        '''
        Sets the equivalence ratio of the undiluted mixture using Cantera
        '''
        equivalence_ratio = float(equivalence_ratio)

        # set the equivalence ratio
        self.undiluted.set_equivalence_ratio(equivalence_ratio,
                                             self.fuel,
                                             self.oxidizer)
        try:
            self.add_diluent(self.diluent, self.diluent_mol_frac)
        except AttributeError:
            pass

        # ensure good inputs were given and record new equivalence ratio
        if sum([self.undiluted.X > 0][0]) < 2:
            print('You can\t detonate that, ya dingus')
            raise ValueError
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
        return Velocity(cj_speed, 'm/s')

    def add_diluent(self, diluent, mole_fraction):
        '''
        Adds a diluent to an undiluted mixture, keeping the same equivalence
        ratio.
        '''
        # make sure diluent is available in mechanism and isn't the fuel or ox
        if diluent not in self.undiluted.species_names:
            print('Bad diluent:', diluent)
            raise ValueError
        elif diluent in [self.fuel, self.oxidizer]:
            print('You can\'t dilute with fuel or oxidizer!')
            raise ValueError
        elif mole_fraction > 1.:
            print('Bro, do you even mole fraction?')
            raise ValueError

        self.diluent = diluent
        self.diluent_mol_frac = mole_fraction

        # collect undiluted mole fractions
        mole_fractions = self.undiluted.mole_fraction_dict()

        # add diluent and adjust mole fractions so they sum to 1
        new_fuel = (1 - mole_fraction) * mole_fractions[self.fuel]
        new_ox = (1 - mole_fraction) * mole_fractions[self.oxidizer]
        x = '{0}: {1} {2}: {3} {4}: {5}'.format(diluent,
                                                mole_fraction,
                                                self.fuel,
                                                new_fuel,
                                                self.oxidizer,
                                                new_ox)
        try:
            # add to diluted cantera solution
            self.diluted.X = x
        except AttributeError:
            # create cantera solution if one doesn't exist
            self.diluted = ct.Solution(self.mechanism)
            self.diluted.TPX = (self.T.value, self.P.value, x)

    def __str__(self):
        return '''
This is my detonation.
There are many like it, but this one is mine.

My detonation is my best friend.
It is my life.
I must master it as I must master my life.

Without me my detonation is useless.
Without my detonation I am useless.
I must initiate my detonation true.
I must initiate better than my academic rivals who are trying to outpublish me.
I must collect data before he collects my data.
I will...

My detonation and I know that what counts in academia is not the detonations
we initiate, the data we collect, nor the analysis we conduct.
We know that it is the impact factors that count.
We will publish...

My detonation is human, even as I, because it is my life.
Thus, I will learn it as a brother.
I will learn its weaknesses, its strength, its parameters, its diluents,
its causes and its effects.
I will keep my detonation tube clean and ready.
We will become part of each other.
We will...

Before Joe Shepherd, I swear this creed.
My detonation and I are defenders of my degree.
We are the masters of our academic rivals.
We are the saviors of my degree.

So be it, until victory is Oregon State's and there is no enemy but data.
'''

    def __repr__(self):
        return str(self)

    def get_mass(self, tube_volume_m3, diluted=False):
        '''
        The cantera concentration function is used to collect
        species concentrations, in kmol/m^3, which are then multiplied by
        the molecular weights in kg/kmol to get the density in kg/m^3. This
        is then multiplied by the tube volume to get the total mass of each
        component.
        '''
        if diluted:
            cantera_solution = self.diluted
        else:
            cantera_solution = self.undiluted
        mixture_list = []
        for i, species in enumerate(cantera_solution.species_names):
            if cantera_solution.X[i] > 0:
                R = 8314 / cantera_solution.molecular_weights[i]
                P = self.P.value * cantera_solution.X[i]
                T = self.T.value
                rho = P/(R*T)
                mixture_list.append([species, rho * tube_volume_m3])
#                mixture_list.append([species,
#                                    cantera_solution.concentrations[i] *
#                                    cantera_solution.molecular_weights[i] *
#                                    tube_volume_m3])
        return dict(mixture_list)

    def get_pressures(self, diluted=False):
        '''
        Cantera is used to get the mole fractions of each species, which are
        then multiplied by the initial pressure to get each partial pressure.
        '''
        if diluted:
            cantera_solution = self.diluted
        else:
            cantera_solution = self.undiluted
        mixture_list = []
        for i, species in enumerate(cantera_solution.species_names):
            if cantera_solution.X[i] > 0:
                mixture_list.append([species,
                                    self.P.value *
                                    cantera_solution.X[i]])
        return dict(mixture_list)


if __name__ == '__main__':
    T = Temperature(20, 'C')
    P = Pressure(1, 'atm')
    test = Detonation(P, T, 'H2', 'O2')

    # check CJ
    from matplotlib import pyplot as plt
    plt.close('all')
    equivs = [i * 0.25 + 0.5 for i in xrange(9)]
    cj_velocities = []
    for phi in equivs:
        # stoich:
        # H2 + 0.5(O2 + 3.76N2) -> H2O + (3.76/2)N2
        # phi = (F/A)/(F/A)st = (A/F)st/(A/F)
        # A/F = (A/F)st / phi = (0.5/1) / phi
        mols_H2 = 1.
        mols_O2 = 0.5 / phi
        mols_N2 = 0.5 / phi * 3.76
        gases = 'H2: {0} O2: {1} N2: {2}'.format(mols_H2, mols_O2, mols_N2)
        [cj, _] = sd.CJspeed(P.to_Pa().value,
                             T.to_Kelvin().value,
                             gases,
                             'gri30.cti',
                             0)
        cj_velocities.append(cj)

    # load in plot from cicarelli and dorofeev
    cj_plot = plt.imread('cj_speeds_original.png')

    # I don't want to have to re-use ginput every run, just copy and paste
    # image coordinates here
    image_coords = [(121.81653225806453, 420.03002016129028),
                    (654.875, 30.42921370967747)]

    # shift calculated values to where they should be on the imported plot
    phi2 = [phi/3. * (image_coords[1][0]-image_coords[0][0]) +
            image_coords[0][0] for phi in equivs]
    cj2 = [v/2500 * (image_coords[1][1]-image_coords[0][1]) +
           image_coords[0][1] for v in cj_velocities]

    # overlay calculated cj velocities
    plt.imshow(cj_plot)
    plt.plot(phi2, cj2, 'rx')
    plt.axis('off')
    plt.savefig('cj_speeds.png')
