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

  a0 = np.array(vs)
  a1 = np.diff(a0, axis=0)
  a1 = a1 / dt
  a2 = a1 * a1
  discomfort = np.sum(a2)

  return discomfort

