#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Assignment 2: Testing for Task 3 and Task4 
Created on 
@author: ashesh
"""

import pickle
import numpy as np
import calc_road_profile as crp
import explore_qc as expl
import optimise_qc as optm

# Parameters: This section contains a list of parameters 
# 
# Parameters for the quarter car 
ms = 250       # The sprung mass 
mu = 35        # The unsprung mass 
kt = 150e3     # The spring constant for the tyre 
# 
# Parameters for the suspension
k = 1000       # The spring constant for the suspension
b = 1500        # The inertance
c = 5000       # The damping coefficient
#
# Parameters for simulation
dt = 0.001     # The time increment 
time_start = 0     # Start time for simulation 
time_end = 2       # End time for simulation 
# 
# Parameters for car travel 
speed = 6      # Speed of the car in m/s
#
# Parameters for the hump 
hump_height = 0.1           # height of the hump in m 
hump_half_width = 1.2        # half width of the hump in m 
distance_between_humps = 10  # distance between humps 
# 

# Parameters for the suspension desgin
b_lower = 100   # Lower search limit for the inerter inertance
b_upper = 1000   # Upper search limit for the inerter inertance
c_lower = 4000  # Lower search limit for the damping coefficient
c_upper = 8000  # Upper search limit for the damping coefficient
inerter_values = 10        # Number of inertances to be used
damper_values = 20         # Number of damping coefficients to be used 

# Create a time array         
time_array = np.arange(time_start, time_end, dt)   

# Get the road profile (using the provided function) 
y_road, x_distance = crp.calc_road_profile(time_array, speed, hump_half_width, 
                                         hump_height, distance_between_humps)

## -----------------------------------------------------------

# Call the function 'explore_qc' (student's implementation!)

inerter_array = np.linspace(b_lower, b_upper, inerter_values)
damping_coefficient_array = np.linspace(c_upper, c_lower, damper_values)


discomfort_array = expl.explore_qc(time_array, y_road, ms, mu, kt, k, 
                                   inerter_array, damping_coefficient_array)

discomfort_upper_limit = 100000
min_inerter, min_damping_coefficient, max_inerter, max_damping_coefficient  = \
    optm.optimise_qc(discomfort_array, inerter_array, damping_coefficient_array, discomfort_upper_limit)


## -----------------------------------------------------------
## -----------------------------------------------------------
# Let's check the values against the reference values

# Load the reference values for the functions simulate_qc  and calc_discomfort
# Read from the file discomfort_array, min_inerter, min_damping_coefficient, max_inerter

f_ref1_task3_task4 = open('ref1_task3_task4.pickle', 'rb')
ref_data = pickle.load(f_ref1_task3_task4) 
discomfort_array_ref = ref_data['discomfort_array']
min_inerter_ref = ref_data['min_inerter']
min_damping_coefficient_ref = ref_data['min_damping_coefficient']
max_inerter_ref = ref_data['max_inerter']
max_damping_coefficient_ref = ref_data['max_damping_coefficient']
f_ref1_task3_task4.close()

# Calculate absolute differences between the reference and actual values
err_discomfort_array        = np.max(np.abs( discomfort_array - discomfort_array_ref ))
err_min_inerter             = np.max(np.abs( min_inerter - min_inerter_ref ))
err_min_damping_coefficient = np.max(np.abs( min_damping_coefficient - min_damping_coefficient_ref ))
err_max_inerter             = np.max(np.abs( max_inerter - max_inerter_ref ))
err_max_damping_coefficient = np.max(np.abs( max_damping_coefficient - max_damping_coefficient_ref ))

# Define tolerance
TOL = 10e-4

# Check differences against the tolerance (TOL)
if ( err_discomfort_array < TOL ):
    print("discomfort_array: Test Passed!")
else :
    print("discomfort_array: Test Failed!")
    print("discomfort_array: Max difference in 'discomfort_array' values: " + str(err_discomfort_array))
    
if ( err_min_inerter < TOL ):
    print("min_inerter: Test Passed!")
else :
    print("min_inerter: Test Failed!")
    print("min_inerter: Difference in min_inerter value: " + str(err_min_inerter))

if ( err_min_damping_coefficient < TOL ):
    print("min_damping_coefficient: Test Passed!")
else :
    print("min_damping_coefficient: Test Failed!")
    print("min_damping_coefficient: Difference in min_damping_coefficient value: " + str(err_min_damping_coefficient))

if ( err_max_inerter < TOL ):
    print("max_inerter: Test Passed!")
else :
    print("max_inerter: Test Failed!")
    print("max_inerter: Difference in max_inerter value: " + str(err_max_inerter))

if ( err_max_damping_coefficient < TOL ):
    print("max_damping_coefficient: Test Passed!")
else :
    print("max_damping_coefficient: Test Failed!")
    print("max_damping_coefficient: Difference in max_damping_coefficient value: " + str(err_max_damping_coefficient))


# ------------------- ------------------ ---------------- ----------- 
# ------------------- ------------------ ---------------- ----------- 
    
