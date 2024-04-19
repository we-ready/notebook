#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: ashesh

Purpose: This function returns the height of road that a vehicle travels
         over. The road consists of humps at regular intervals. 

Input:
   time_array                time_array
   speed                     speed of the car
   hump_half_width           half-width of the hump
   hump_height               height of the hump
   distance_between_humps    distance between consecutive humps

 Output:
   y_road                   (array) height of the road 
   x_distance               (array) horizontal distance of the car from the
                            starting position 


"""
import numpy as np

def calc_road_profile(time_array, speed, hump_half_width, hump_height, 
                    distance_between_humps) :
   
    # We assume that the hump is a sector of a circle 
    # Given the height and width, the radius is given by the following formula
    hump_radius = (hump_half_width ** 2) /( 2 * hump_height)
    
    # This is to map the horizontal distance to a value in
    # [-hump_half_width, hump_half_width]
    # The distance is also shifted by distance_between_humps/2 so that 
    # the car starts at 0 level 
    
    val1 = (speed*time_array % distance_between_humps)
    x_distance_mod = np.maximum(np.minimum(val1 - distance_between_humps/2, hump_half_width), - 
                                hump_half_width )    

    # This maps the wrapped distance to the height of the hump
    y_road = hump_radius * np.cos(np.arcsin(x_distance_mod/hump_radius)) - hump_radius + hump_height       

    # Calculate xDistance 
    x_distance = speed * time_array; 

    return y_road, x_distance


    
