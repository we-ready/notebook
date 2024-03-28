#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on --INSERT DATE HERE--

@author: -- INSERT NAME HERE --

"""


def calculate_similarity(data_segment, pattern):
    """ Calculate the similarity between one data segment and the pattern.

    Parameters
    ----------
    data_segment : [float]
        A list of float values to compare against the pattern.

    pattern : [float]
        A list of float values representing the pattern. 

    Returns
    -------
    float
        The similarity score/value.
        
    "Error"
        If data segment and pattern are not the same length.

    """

    # TODO: Insert your code here.

    if len(data_segment) != len(pattern):
        return "Error"
    
    rslt = 0
    for i in range(len(pattern)):
        rslt = rslt + data_segment[i] * pattern[i]
    return rslt
