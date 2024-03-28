#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on --INSERT DATE HERE--

@author: -- INSERT NAME HERE --

"""

from calculate_similarity_list import calculate_similarity_list

def pattern_search_max(data_series, pattern, threshold):
    """ Search for the highest similarity measure that is also greater than
        or equal to the given threshold value and returns the index of that
        value.

        The function finds the index of the highest similarity value,
        using the similarity_list returned by the function
        'calculate_similarity_list'.

    Parameters
    ----------
    data_series : [float]
        A list of float values representing a data series.

    pattern : [float]
        A list of float values representing the pattern.

    threshold : [float]
        A float value. Selected similarity measure needs to be greater than or
        equal to the given threshold value.

    Returns
    -------
    "Insufficient data" : [String]
        If the given data_series is shorter than the given pattern.

    "Not detected" : [String]
        If all the similarity measures are (strictly) less than the given
        threshold value.

    integer
        Index of the highest similarity measure that is also greater than
        or equal to the given threshold value.
    """

    # TODO: Insert your code here.

    if len(data_series) < len(pattern):
        return "Insufficient data"
    
    arr = calculate_similarity_list(data_series, pattern)
    max_index = arr.index(max(arr))
    max_value = arr[max_index]
    if max_value >= threshold:
        return max_index
    else:
        return "Not detected"
