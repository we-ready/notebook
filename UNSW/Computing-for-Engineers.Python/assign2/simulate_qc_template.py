#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 08:38:08 2019

@author:  

Purpose: To simulate a quarter car based on the 
         model described in the assignment

Inputs:
   time   time_array
   y_road  an array of road heights
   ms     the mass of 1/4 of the car body
   mu     the mass of the tyre and wheel
   kt     tyre stiffness
   k      spring stiffness
   b      inertance
   c      damping coefficient

Outputs:
  ys     the verticle displacement of the center of the car body 
         from a reference level
  yu     the verticle displacement of the center of the wheel/tyre 
         from a reference level
  vs     the verticle velocity of the quarter car body       
  vu     the verticle velocity of the wheel/tyre
    
    
"""    

import numpy as np 
   

def simulate_qc(time_array, y_road, ms, mu, kt, k, b, c) : 

    # Calculate time increment (dt)
    dt = time_array[1] - time_array[0]
    

    
    
    return ys, yu, vs, vu 
    
 

