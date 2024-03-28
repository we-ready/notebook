#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: addo, modified by ashesh

"""
import calculate_similarity as cs

# ------- TEST CASES ------------------
# Some example test data defined below.
# You need to create some more of your own.
# Copy the format, but change the values.
# To change which test case is used, skip below to the main module.
def test1():
    """
    Example from the assignment spec.
    """
    data_segment = [-1, 2, -2, 3]
    pattern = [40, 30, 20, 10]

    expected_answer = 10

    return data_segment, pattern, expected_answer


def test2():
    """
    This should be an error because the size of the data SEGMENT (not series) is
    not equal to the size of the pattern list.
    """
    data_segment = [-1, 2, -2, 3]
    pattern = [40, 30, 20]

    expected_answer = "Error"

    return data_segment, pattern, expected_answer


# --- CHECK OUTPUT ------------------
# This function compares the value of two lists.
# Check your output against expected output, and report the result
def check_output(result, expected_answer):

    # Let's print your output
    print('This is the output your function gave --> ', result)
    # Let's print expected output
    print('This is the expected output --> ', expected_answer)

    # Let's check whether 'result' is string or not?
    if isinstance(result, str):
        if(result == expected_answer):
            print('GOOD JOB your output matches the expected outputs. YAY!!!!! =)')
            return
        else:
            print('Oh noooo, your output does NOT match expected output. Please try again.')
            return

    TOL = 0.00001       
    if abs(result - expected_answer) < TOL:
            print('GOOD JOB your output matches the expected outputs. YAY!!!!! =)')
    else:
            print('Oh noooo, your output does NOT match expected output. Please try again.')



# ---- MAIN MODULE --------------------
# This is the main code that performs the test
print('TESTING FUNCTION: calculate_similarity')

# Select Your Test, you can select one at a time
# TODO change the test<number> to run a different test at a time
data_segment, pattern, expected_answer = test1()
#data_segment, pattern, expected_answer = test2()

# Let's call your function!
result = cs.calculate_similarity(data_segment, pattern)

# Let's check your output against expected output, and report the result
check_output(result, expected_answer)

# -------- end ---------------
