#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: 
    

Purpose:
   Determining the discomfort levels for a given damper values and inerter values

Inputs:
   time   time_array
   y_road  an array of road heights
   ms     the mass of 1/4 of the car body
   mu     the mass of the tyre and wheel
   kt     tyre stiffness
   k      spring stiffness
   inerter_values              inertance values (array of type float)
   damping_coefficient_values  damping coefficient values (array of type float)

Output:
   discomfort_array   2-dimentional numpy array with discomfort values for 
                      given damper values and inerter values (read the specs)
   
"""

import numpy as np
import calc_discomfort as cd
import simulate_qc as sqc


def explore_qc(time_array, y_road, ms, mu, kt, k,
               inerter_array, damping_coefficient_array):

  # Calculate dt from time_array
  dt = time_array[1] - time_array[0]

  # Initialise 2 dimentional discomfort_array
  discomfortLevels = np.zeros(
      (len(inerter_array), len(damping_coefficient_array)), dtype=np.float64)

  # Iterate over inerter_array
  (rows, cols) = discomfortLevels.shape
  for i in range(rows):
    for j in range(cols):
      ys, yu, vs, vu = sqc.simulate_qc(time_array, y_road, ms, mu, kt, k,
                                       inerter_array[i],
                                       damping_coefficient_array[j])
      discomfortLevels[i, j] = cd.calc_discomfort(vs, dt)

  return discomfortLevels
