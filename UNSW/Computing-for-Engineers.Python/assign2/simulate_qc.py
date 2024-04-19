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
   
def simulate_qc(time_array, y_road, ms, mu, kt, k, b, c):

  # initial output array
  ys = np.zeros_like(time_array)
  yu = np.zeros_like(time_array)
  vs = np.zeros_like(time_array)
  vu = np.zeros_like(time_array)
  # print(ys, yu, vs, vu)

  # Iterate
  for i in range(0,len(time_array)-1):
    ft = funcF(vs[i], vu[i], ys[i], yu[i], k, c)
    ht = ft - kt * yu[i] + kt * y_road[i]

    dt = time_array[i+1] - time_array[i]
    ys[i+1] = ys[i] + vs[i] * dt
    yu[i+1] = yu[i] + vu[i] * dt
    vs[i+1] = vs[i] + funcDeltaVs(ft, ht, dt, ms, mu, b)
    vu[i+1] = vu[i] + funcDeltaVu(ft, ht, dt, ms, mu, b)
    
  return ys, yu, vs, vu

def funcF(vs, vu, ys, yu, k, c):
  return c * vs - c * vu + k * ys - k * yu

def funcDeltaVs(ft, ht, dt, ms, mu, b):
  a = -1 * (mu + b) * ft + b * ht
  b = ms * mu + (ms + mu) * b
  return (a / b) * dt

def funcDeltaVu(ft, ht, dt, ms, mu, b):
  a = -1 * b * ft + (ms + b) * ht
  b = ms * mu + (ms + mu) * b
  return (a / b) * dt
