#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: addo, modified by ashesh

"""
import calculate_similarity_list as csl

# ------- TEST CASES ------------------
# Some example test data defined below.
# You need to create some more of your own.
# Copy the format, but change the values.
# To change which test case is used, skip below to the main module.
def test1():
    """
    An example from the assignment spec.
    """
    data_series = [-1, 2, -2, 3, 41, 38, 22, 10, -1, 3]
    pattern = [40, 30, 20, 10]

    expected_answer = [10, 490, 1210, 2330, 3320, 2370, 1190]

    return data_series, pattern, expected_answer


def test2():
    """
    A slightly more elaborate example. Remember you need to handle floats
    as well as negative numbers in either of the lists.
    """
    data_series = [-1, 2, 21, 15, -30.34, 38, 22.2, 4]
    pattern = [5, -1, 3]

    expected_answer = [56, 34, -1.02, 219.34, -123.1, 179.8]

    return data_series, pattern, expected_answer


###################################################

# --- CHECK OUTPUT ------------------
# This function compares the value of two lists.
# Check your output against expected output, and report the result
def check_output(result, expected_answer):
    # Let's check whether the parameters are lists or not?
    if not((type(result) is list) and (type(expected_answer) is list)):
        print("Error: invalid input for the function 'check_output' ")
        return

    # Let's print your output
    print('This is the output your function gave --> ', result)
    # Let's print expected output
    print('This is the expected output --> ', expected_answer)

    if len(result) != len(expected_answer):
        print('Oh noooo, your output does NOT match expected output. Please try again.')
        return

    TOL = 0.00001
    is_correct = True
    for i in range(0, len(expected_answer)):
        if isinstance(result[i], str) :
                is_correct = False        
        elif  abs(result[i] - expected_answer[i]) > TOL:
                is_correct = False

    if is_correct is True:
            print('GOOD JOB your output matches the expected outputs. YAY!!!!! =)')
    else:
            print('Oh noooo, your output does NOT match expected output. Please try again.')


# ---- MAIN MODULE --------------------
# This is the main code that performs the test
print('TESTING FUNCTION: calculate_similarity_list')

# Select Your Test, you can select one at a time
# TODO change the test<number> to run a different test at a time
data_series, pattern, expected_answer = test1()
#data_series, pattern, expected_answer = test2()

# Let's call your function!
result = csl.calculate_similarity_list(data_series, pattern)

# Let's check your output against expected output, and report the result
check_output(result, expected_answer)

# -------- end ---------------
