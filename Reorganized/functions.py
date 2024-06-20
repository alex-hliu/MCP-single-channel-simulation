from math import *
import numpy as np
from initial_conditions import *

#Helper Functions
def vector(x, y, z):
    return np.array([x, y, z] , dtype = np.float64)

def mag(vector):
    return sqrt(sum(pow(element, 2) for element in vector))

def mag2(vector):
    return pow(mag(vector), 2)

def unit(vector):
    if mag(vector) == 0:
        return 0
    return vector / mag(vector)

def force(force):
    return vector(0, 0, -force)

def split():
    split_count = np.random.poisson(4)
    while split_count < 1:
        split_count = np.random.poisson(4)
    return split_count
