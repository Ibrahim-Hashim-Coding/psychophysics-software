"""
@author Ibrahim Che Hashim
@email ibrahimhashim.coding@gmail.com/coding.hashim@gmail.com

Script containing functions for staircases for the DeWeerd Lab Psychophysics Software

Last edited: 01/06/2020 by Ibrahim Che Hashim
Saved on github under https://github.com/Ibrahim-Hashim-Coding/psychophysics-software
"""

# Import libraries needed to run
import random


# This function calculates the angle at which the stimulus grating will be tilted away from the reference orientation_list
# and returns both the direction (-1 or 1 e.g. left or right) and the orientation
def calculate_grating_orientation(reference_orientation, current_orientation):
    grating_direction = random.choice([-1, 1])
    grating_orientation = reference_orientation + current_orientation*grating_direction
    return grating_orientation, grating_direction


def calculate_number_reversals(number_reversals, movement_direction, last_direction):
    if movement_direction == 'no_change':
        pass
    elif last_direction == 'not_set_yet':
        last_direction = movement_direction
    elif movement_direction != last_direction:
        last_direction = movement_direction
        number_reversals -= 1
    return number_reversals, movement_direction, last_direction


# This function determines whether the orientation_list_counter has to be increased, decreased or kept the same
def calculate_orientation_list_counter(orientation_list_counter, movement_direction, length_orientation_list):
    if movement_direction == 'no_change':
        pass
    elif movement_direction == 'up':
        if orientation_list_counter != 0:
            orientation_list_counter -= 1
    elif movement_direction == 'down':
        if orientation_list_counter != length_orientation_list:
            orientation_list_counter += 1
    return orientation_list_counter


# This function returns whether the response of the user was correct or not
def calculate_response(key_pressed, grating_direction):
    if key_pressed == 'left':
        if grating_direction == -1:
            response = 1  # indicates correct answer
        else:
            response = -1  # indicates wrong answer
    elif key_pressed == 'right':
        if grating_direction == 1:
            response = 1  # indicates correct answer
        else:
            response = -1  # indicates wrong answer
    else:
        response = 0  # indicates no response or wrong key pressed
    return response


# This function creates all the changes in orientation required by the user. The orientations will be used to modify the 
# reference orientation set by the user.
def create_orientation_list(maximum_value, division_value, length_list,):
    orientation_list = [round(float(maximum_value)/(float(division_value)**float(x)), 3) if x != 0 else float(maximum_value) for x in range(0, length_list)]
    return orientation_list


# This function creates and returns two empty lists.
def reset_staircase_counters():  # sets both list counters back to empty
        staircase_counter_1 = []
        staircase_counter_2 = []
        return staircase_counter_1, staircase_counter_2


# This function updates the staircase counters and decides whether the staircase should be moving up or down based on the 
# number of correct and wrong answer a participant has given.
def update_staircase_count(staircase_counter_up, staircase_counter_down, n_up, n_down, response):
    if response == 1:  # if correct response
        staircase_counter_down.append(1)
    elif response == -1:  # if wrong response
        staircase_counter_up.append(1)

    if sum(staircase_counter_down) == n_down:  # if correct answers is equal to number down return down direction
        movement_direction = 'down'
        staircase_counter_up, staircase_counter_down = reset_staircase_counters()  # if wrong answers is equal to number up return down direction
    elif sum(staircase_counter_up) == n_up:
        movement_direction = 'up'
        staircase_counter_up, staircase_counter_down = reset_staircase_counters()  
    else:
        movement_direction = 'no_change'  # if neither of two conditions above have been achieved

    return(staircase_counter_up, staircase_counter_down, movement_direction)
