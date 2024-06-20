from math import *
import matplotlib.pyplot as plt
import numpy as np

from Channel import Channel
from Electron import Electron
from functions import vector, split
from units import *
from initial_conditions import *

#Lists for simulation
act_electrons         = []
output_electrons      = []
backsplash_electrons  = []

#Initial electron setup
v0  = sqrt((2 * ev0) / mass_Mevc2)

#Units in mm/nsec
v0  = v0 * c
vx0 = v0 * sin(theta0) * cos(phi0)
vy0 = v0 * sin(theta0) * sin(phi0)
vz0 = v0 * cos(theta0)

initial_velocity = vector(vx0, vy0, vz0)

initial_electron = Electron(position= vector(0 , 0 , 0), velocity= initial_velocity,
                            time= t, update_flag= False, creation_time= t)

act_electrons.append(initial_electron)

channel = Channel(position= vector(0, 0, 0), axis= vector(0, 0, channel_length), radius= channel_radius)

snd_emission_energy = []



while True:
    t = t + dt

    #Temporary lists
    secondary_emission_electrons = []
    temp_backsplash = []
    temp_output_electrons = []

    temp_backsplash       = [electron for electron in act_electrons if electron.check_backsplash()]
    backsplash_electrons.extend(temp_backsplash)

    temp_output_electrons = [electron for electron in act_electrons if electron.end_reached(channel)]
    output_electrons.extend(temp_output_electrons)

    act_electrons[:]      = [electron for electron in act_electrons if not electron.check_backsplash() and not electron.end_reached(channel)]

    if len(act_electrons) == 0:
        print("gain", len(output_electrons))
        print("time", t)

        energy_avg = 0
        energy_list = []
        for i in output_electrons:
            energy_list.append(i.energy())
            energy_avg += i.energy()

        energy_avg = energy_avg / len(output_electrons)

        print("AVG_output_electron_KE(MeV): ", energy_avg)

        #plt.hist(energy_list)
        #plt.show()

        quit()

    #Loops over the active electrons and update its properties
    for electron in act_electrons:

        #if its at the boundry under the conditions of check_boundry then a secondary_emission_vector function will be
        # called that modifies the velocity of the electron
        if electron.check_boundry(channel):
            split_count = split()
            original_position = electron.position

            #Adjusting the incident electron's properties including position and velocity after the contant with channel
            new_velocity_vector = electron.secondary_emission_vector(channel, split_count)
            electron.velocity = new_velocity_vector
            electron.update_position()

            new_electrons = []

            #Creating new electrons and appending them to a list outside of the parent for loop, the position is the
            #original position of the parent electron with the new velocity vector.
            #The [1:] is to minus 1 from the count so that if the split count is two, 1 is removed to account for the
            #original electron.
            for i in range(split_count)[1:]:
                new_electron = Electron(position= original_position, velocity= new_velocity_vector, time= t,
                                        update_flag= False, creation_time= t)
                new_electrons.append(new_electron)

                secondary_emission_electrons.extend(new_electrons)

            #So that it won't update position and velocity twice
            continue

        electron.update_pos_vel()

    #TESTING
    print("SE count:         ", len(secondary_emission_electrons), t)
    print("Active Electrons: ", len(act_electrons))
    print("velocity:         ", act_electrons[0].velocity)
    print("position:         ", act_electrons[0].position)


    act_electrons.extend(secondary_emission_electrons)
