#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: 
    
Purpose:
   Determining the discomfort levels for a given damper values and inerter values

Inputs:
   discomfort_array   2-dimentional numpy array with discomfort values for 
                      given inerter_values and damping_coefficient_values (read the specs)    
   inerter_values     inertance values (array of type float)
   damping_coefficient_values  damping coefficient values (array of type float)
   discomfort_upper_limit      maximum discomfort value to calculate worst comfort
                               (i.e. 'max_inerter' and 'max_damping_coefficient' values)
   

Output:
    min_inerter and min_damping_coefficient  the pair that gives the smallest value of discomfort  
    max_inerter and max_damping_coefficient  the pair that gives the worst value of discomfort, that
                                             is less than or equal to a given 'discomfort_upper_limit'
   
"""

import numpy as np

def optimise_qc(discomfort_array, inerter_array, damping_coefficient_array, discomfort_upper_limit):

  a = np.array(discomfort_array)
  idxMin = np.unravel_index(a.argmin(), a.shape)

  a[a > discomfort_upper_limit] = 0
  idxMax = np.unravel_index(a.argmax(), a.shape)

  return inerter_array[idxMin[0]], damping_coefficient_array[idxMin[1]], \
          inerter_array[idxMax[0]], damping_coefficient_array[idxMax[1]]
