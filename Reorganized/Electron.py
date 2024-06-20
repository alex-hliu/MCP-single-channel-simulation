import numpy as np
from math import *
from functions import *
from initial_conditions import *

# Physics Functions for Electron Behavior
class Electron():
    def __init__(self, position, velocity, time, update_flag, creation_time):
        self.position            = position
        self.velocity            = velocity
        self.time                = time
        self.update_flag         = update_flag
        self.creation_time       = creation_time #Time since creation of electron on simulation start time

    #Simulation functions
    def flag_true(self):
        self.update_flag = True

    def flag_false(self):
        self.update_flag = False

    def check_backsplash(self):
        return self.position[2] > 1.0

    def end_reached(self, confine):
        return self.position[2] <= confine.axis[2]

    #Physics functions
    def energy(self):
        velocityMagnitude = mag(self.velocity)
        KE = (1/2) * mass_Mevc2 * pow(velocityMagnitude, 2)
        return KE

    @staticmethod
    def radius_calculation(position, confine):
        #Projection Formula
        projection = (np.dot(position, confine.axis) / mag2(confine.axis)) * confine.axis
        radius     = position - projection
        return radius
        # The returned radius should be a vector with the x and y axis to equal to 0,
        # under the condition where the axis of the channel is perpendicular to the xy plane

    #Under all circumstances, update position will come before update velocity because check_boundry
    #is implemented by checking if the next update will cause the electron to hit the boundry under
    #the condition that the velocity is the current velocity.

    def update_position(self):
        self.position = self.position + self.velocity * dt

    def update_velocity(self):
        acceleration   = force(force_parameter) / mass_Mevc2
        self.velocity  = self.velocity + (acceleration * dt)

    #Use this because this ensures that position is updated before updating velocity
    def update_pos_vel(self):
        self.update_position()
        self.update_velocity()

    def check_boundry(self, confine): #This checks if the next update in position due to current velocity will hit boundry
        future_position = self.position + self.velocity * dt
        future_radius   = self.radius_calculation(future_position, confine)

        if mag(future_radius) >= channel_radius:
            self.update_flag = True
            return True

    def secondary_emission_angle(self, confine): #The angle is a unit vector
        radius = self.radius_calculation(self.position, confine)
        normal = unit(-radius)
        reflectionUnitVector = unit(self.velocity - 2 * np.dot(self.velocity, normal) * normal)
        return reflectionUnitVector

    def secondary_emission_vector(self, confine, split_count):
        new_velocity = sqrt((2 * self.energy() * energy_reduction) / (mass_Mevc2 * split_count)) * self.secondary_emission_angle(confine)
        return new_velocity

