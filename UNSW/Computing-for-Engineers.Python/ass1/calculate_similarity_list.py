#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on --INSERT DATE HERE--

@author: -- INSERT NAME HERE --

"""

from calculate_similarity import calculate_similarity


def calculate_similarity_list(data_series, pattern):
    """ Calculate the similarity measures between all possible data segments
    and the pattern.

    The function calculates the similarity measures, using the 
    function 'calculate_similarity', of all possible data segments in a 
    data_series against a given pattern and returns the list of calculated 
    similarity values.

    Parameters
    ----------
    data_series : [float]
        A list of float values representing a data series. 
        
    pattern : [float]
        A list of float values representing the pattern. 

    Returns
    -------
        List of floats
            The list of calculated similarity values.

    """

    # TODO: Insert your code here.
    rslt = []
    size = len(pattern)
    for i in range(len(data_series) - size + 1):
        r = calculate_similarity(data_series[i:i+size], pattern)
        rslt.append(r)
    return rslt
  