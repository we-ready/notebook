#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: addo

"""
import pattern_search_max as psm

# ------- TEST CASES ------------------
# Some example test data defined below.
# You need to create some more of your own.
# Copy the format, but change the values.
# To change which test case is used, skip below to the main module.
def test1():
    """
    Example from the assignment spec.
    The similarity list should be [10, 490, 1210, 2330, 3320, 2370, 1190]
    The highest number of that list is in index 4.
    Remember, indices in lists start at 0. ie: The first value is at index 0.
    """
    data_series = [-1, 2, -2, 3, 41, 38, 22, 10, -1, 3]
    pattern = [40, 30, 20, 10]
    threshold = 15

    expected_answer = 4

    return data_series, pattern, threshold, expected_answer


def test2():
    """
    Case of insufficient data.
    """
    data_series = [-1, 2]
    pattern = [40, 30, 20]
    threshold = 15

    expected_answer = "Insufficient data"

    return data_series, pattern, threshold, expected_answer


def test3():
    """
    Threshold is too high here.
    """
    data_series = [-1, 2, -2, 3, 41, 38, 22, 10, -1, 3]
    pattern = [40, 30, 20, 10]
    threshold = 3321

    expected_answer = "Not detected"

    return data_series, pattern, threshold, expected_answer



# --- CHECK OUTPUT ------------------
# This function compares the value of two lists.
# Check your output against expected output, and report the result
def check_output(result, expected_answer):

    # Let's print your output
    print('This is the output your function gave --> ', result)
    # Let's print expected output
    print('This is the expected output --> ', expected_answer)

    is_correct = True
    if result != expected_answer:
        is_correct = False

    if is_correct is True:
            print('GOOD JOB your output matches the expected outputs. YAY!!!!! =)')
    else:
            print('Oh noooo, your output does NOT match expected output. Please try again.')


# ---- MAIN MODULE --------------------
# This is the main code that performs the test
print('TESTING FUNCTION: pattern_search_max')

# Select Your Test, you can select one at a time
# TODO change the test<number> to run a different test at a time
data_series, pattern, threshold, expected_answer = test1()
#data_series, pattern, threshold, expected_answer = test2()
#data_series, pattern, threshold, expected_answer = test3()

# Let's call your function!
result = psm.pattern_search_max(data_series, pattern, threshold)

# Let's check your output against expected output, and report the result
check_output(result, expected_answer)

# -------- end ---------------
