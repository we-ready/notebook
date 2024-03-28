#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ashesh

"""

import pattern_search_multiple as psm
import matplotlib.pyplot as plt


# ------- TEST CASES ------------------
# Some example test data defined below.
# You need to create some more of your own.
# Copy the format, but change the values.
# To change which test case is used, skip below to the main module.

def test1():
    threshold = 15
    pattern_width = 4
    data_values = [-1, 5, 4, 8, 3, 21, 18, 16, 3, 2, 3, 1, 4, 5, 17, 22, 36, 33, 34, 9, 1, -2]
    data_values = data_values + [-2, 4, -1, 7, 13, 12, 3, 1, 4, 5, 26, 22, 28, 27, 26, 2, 8, 6]

    expected_answer = [5, 16, 34]

    return threshold, pattern_width, data_values, expected_answer


def test2():
    threshold = 10
    pattern_width = 3
    data_values = [-1, 5, 4, 8, 3, 21, 18, 16, 3, 2, 3, 1, 4, 5, 17, 22, 36, 33, 34, 9, 1, -2]
    data_values = data_values + [-2, 4, -1, 7, 13, 12, 3, 1, 4, 5, 26, 22, 28, 27, 26, 2, 8, 6]

    expected_answer = [5, 16, 26, 34]

    return threshold, pattern_width, data_values, expected_answer


# --- CHECK OUTPUT ------------------
# This function compares the value of two lists.
# Check your output against expected output, and report the result
def check_output(selected_indices, expected_answer):
    # Let's check whether the parameters are lists or not?
    if not((type(selected_indices) is list) and (type(expected_answer) is list)):
        print("Error: invalid input for the function 'check_output' ")
        return

    # Let's print your output
    print('This is the output your function gave --> ', selected_indices)
    # Let's print expected output
    print('This is the expected output --> ', expected_answer)

    if len(selected_indices) != len(expected_answer):
        print('Oh noooo, your output does NOT match expected output. Please try again.')
        return

    is_correct = True
    for i in range(0, len(expected_answer)):
        if abs(selected_indices[i] - expected_answer[i]) > 0.00001:
                is_correct = False

    if is_correct is True:
            print('GOOD JOB your output matches the expected outputs. YAY!!!!! =)')
    else:
            print('Oh noooo, your output does NOT match expected output. Please try again.')


# --- plot_results ------------------
# This is just a helper function that graphs the results.
# Let's plot the data_values, the threshold line
# and the seleted indices (green circles)
def plot_results(data_values, selected_indices, threshold):

    # Let's check whether the first two parameters are lists or not?
    if not((type(data_values) is list) and (type(selected_indices) is list)):
        print("Error: invalid input for the function 'plot_results' ")
        return

    selected_values = [ data_values[i] for i in selected_indices]
    threshold_list = [threshold] * len(data_values)
    x_list = [ i for i in range(0,len(data_values))]

    width = 1/2.5
    plt.grid(True)
    plt.rc('grid', linestyle="-", color='lightgray')
    plt.rc('axes', axisbelow=True)
    plt.bar(x_list, data_values, width)
    plt.plot(x_list, threshold_list, 'r' )
    plt.plot(selected_indices, selected_values,'go',label='Peaks')
    plt.xlabel('index')
    plt.ylabel('data values')
    plt.title('Fig: pattern_search_multiple \n(threshold = ' + str(threshold) + ', pattern_width = ' + str(pattern_width) + ')') # title of the graph
    plt.minorticks_on()
    plt.grid(b=True, which='major',linestyle='-')
    plt.show()
# --------------------------------


# ---- MAIN MODULE --------------------
# This is the main code that performs the test
print('TESTING FUNCTION: pattern_search_multiple')

# Select Your Test, you can select one at a time
# TODO change the test<number> to run a different test at a time
threshold, pattern_width, data_values, expected_answer = test1()
# threshold, pattern_width, data_values, expected_answer = test2()

# Let's call your function!
selected_indices = psm.pattern_search_multiple(data_values, pattern_width, threshold)

# Let's check your output against expected output, and report the result
check_output(selected_indices, expected_answer)

# ------------------------------------------------
# Let's plot the data_values, the threshold line
# and the seleted indices (green circles)
plot_results(data_values, selected_indices, threshold)

# -------- end ---------------
