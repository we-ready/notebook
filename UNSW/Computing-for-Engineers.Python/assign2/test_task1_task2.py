#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Assignment 2: Testing for Task 1 and Task2 
Created on 
@author: ashesh
"""

import pickle
import numpy as np
import simulate_qc as sqc
import calc_road_profile as crp
import calc_discomfort as cd

# Load the reference values for the functions simulate_qc  and calc_discomfort
# Read from the file ys_ref, yu_ref, vs_ref, vu_ref and discomfort_ref
f_ref1_task1_task2 = open('ref1_task1_task2.pickle', 'rb')
ref_data = pickle.load(f_ref1_task1_task2) 
ys_ref = ref_data['ys_ref']
yu_ref = ref_data['yu_ref']
vs_ref = ref_data['vs_ref']
vu_ref = ref_data['vu_ref']
discomfort_ref = ref_data['discomfort_ref']
f_ref1_task1_task2.close()

# Parameters: This section contains a list of parameters 
# 
# Parameters for the quarter car 
ms = 250;       # The sprung mass 
mu = 35;        # The unsprung mass 
kt = 150e3;     # The spring constant for the tyre 
# 
# Parameters for the suspension
k = 1000;       # The spring constant for the suspension
b = 1500;        # The inertance
c = 5000;       # The damping coefficient
#
# Parameters for simulation
dt = 0.001;     # The time increment 
time_start = 0;     # Start time for simulation 
time_end = 2;       # End time for simulation 
# 
# Parameters for car travel 
speed = 6;      # Speed of the car in m/s
#
# Parameters for the hump 
hump_height = 0.1;           # height of the hump in m 
hump_half_width = 1.2;        # half width of the hump in m 
distance_between_humps = 10;  # distance between humps 
# 

# Create a time array          
time_array = np.arange(time_start, time_end, dt)   

# Get the road profile (using the provided function) 
y_road, x_distance = crp.calc_road_profile(time_array, speed, hump_half_width, 
                                         hump_height, distance_between_humps)

## -----------------------------------------------------------

# Call the function 'simulate_qc' (student's implementation!)
ys, yu, vs, vu = sqc.simulate_qc(time_array, y_road, ms, mu, kt, k, b, c)

# Call the function 'calc_discomfort' (student's implementation!)
discomfort = cd.calc_discomfort( vs_ref , dt )

## -----------------------------------------------------------

## -----------------------------------------------------------
# Let's check the values against the reference values

# Calculate absolute differences between the reference and actual values

err_ys = np.max(np.abs( ys - ys_ref ));
err_yu = np.max(np.abs( yu - yu_ref ));
err_vs = np.max(np.abs( vs - vs_ref ));
err_vu = np.max(np.abs( vu - vu_ref ));
err_discomfort = abs(discomfort_ref - discomfort)


# Define tolerance
TOL = 10e-4;

# Check differences against the tolerance (TOL)
if ( err_ys < TOL ):
    print("ys: Test Passed!")
else :
    print("ys: Test Failed!")
    print("ys: Max difference in ys values: " + str(err_ys))
    
if ( err_yu < TOL ):
    print("yu: Test Passed!")
else :
    print("yu: Test Failed!")
    print("yu: Max difference in yu values: " + str(err_yu))

if ( err_vs < TOL ):
    print("vs: Test Passed!")
else :
    print("vs: Test Failed!")
    print("vs: Max difference in vs values: " + str(err_vs))
    
if ( err_vu < TOL ):
    print("yu: Test Passed!")
else :
    print("vu: Test Failed!")
    print("vu: Max difference in vu values: " + str(err_vu))
    
if ( err_discomfort < TOL ):
    print("discomfort: Test Passed!")
else :
    print("discomfort: Test Failed!")
    print("discomfort: Difference in discomfort value: " + str(err_discomfort))
    
    
# ------------------- ------------------ ---------------- ----------- 
# ------------------- ------------------ ---------------- ----------- 
    
