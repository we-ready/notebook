#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: 
    

Purpose:
   Determining the discomfort level for a given set of suspension parameters

Inputs:
  vs    the verticle velocity of the quarter car body       
  dt    time increment 

Output:
   discomfort: a scalar representing the discomfort level for the given
   vehicle and suspension parameters
       
"""
import numpy as np

def calc_discomfort(vs, dt):

  # initial array
  a2 = np.zeros_like(vs)

  # Iterate
  for i in range(0, len(vs) - 1):
    ai = (vs[i + 1] - vs[i]) / dt
    a2[i] = ai * ai

  discomfort = np.sum(a2)
  return discomfort


