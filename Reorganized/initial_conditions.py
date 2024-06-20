from math import *
from units import *

#Monte Carlo
t                = 0
dt               = 0.01

#Simulation Conditions
energy_reduction = 1
sigma            = pi/8

#Initial Electron Conditions
mass             = 0.5109989461*MeVc2
mass_Mevc2       = 0.5109989461
q                = -1.6*10**-19 #Charge of an electron (CAREFUL THE SIGN IS POSITIVE FOR CALCULATION PURPOSES)
ev0              = 800 * eV
voltage          = 800

#degree off axis of going straight down the axis of the channel
initial_electron_degree = 20

#Coordinate used: https://en.wikipedia.org/wiki/File:3D_Spherical.svg
theta0           = pi + initial_electron_degree * pi/180
phi0             = 0

#Channel Conditions
channel_radius   = 20*um
channel_length   = -4*mm

#Force Calculation from Initial Conditions (for use in Electron.py line 37)
#Unit in kgm/s^2
force_parameter = q * voltage * meter**2 / channel_length

#Unit Conversion to evmm/nsec^2
force_parameter = force_parameter * kg * (1/sec**2)



