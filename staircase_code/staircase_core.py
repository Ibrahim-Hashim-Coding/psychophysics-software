'''
@author Ibrahim Che Hashim
@email ibrahimhashim.coding@gmail.com/coding.hashim@gmail.com

Script containing the core function for the staircase option in the DeWeerdLab psychophysics software

Last edited: 01/06/2020 by Ibrahim Che Hashim
Saved on github under https://github.com/Ibrahim-Hashim-Coding/psychophysics-software


STORING DATA -> 
store log + data file in individual file, labeled with participant id and time + date

DeWeerd Lab Psychophysics Software -> Users -> User A -> Parameter Files 
                                                         Data -> Parameter File Names -> Participant ID -> Log File and Data File

'''
from psychopy import visual, event, core
import staircase_functions

# set staircase values
number_reversals = 2  # if this reaches 0, staircase ends
number_trials = 1  # if this reaches 0, staircase ends
n_up = 1
n_down = 4
trial_counter = 0

# create orientation list and setting reference orientation_list
reference_ori = -45
ori_list_length = 28
ori_list_max = 22.5
ori_list_div = 1.2
ori_list_created = staircase_functions.create_orientation_list(ori_list_max, ori_list_div, ori_list_length)
ori_list_counter = 0

# create window and obtain data
win = visual.Window([1600,900],allowGUI=True, monitor='testMonitor', units='deg', fullscr = True) # This defines the parameters for the WINDOW where stimuli are shown
win_fps = round(win.getActualFrameRate(), 0)  # gets frame rate of pc and rounds (usually to 60 or 30 - easier to work with then 59.93 or so)

# create fixation stimuli
fix_neutral = visual.GratingStim(win, color = [1,1,1], colorSpace = 'rgb', tex = None, mask = 'circle', units = 'cm', size = 0.2, pos = (0, 0)) # Paramters of FIXATION DOT continuously presented
fix_correct = visual.GratingStim(win, color = [0,1,0], colorSpace = 'rgb', tex = None, mask = 'circle', units = 'cm', size = 0.2, pos = (0, 0)) # Paramters of FIXATION DOT continuously presented
fix_wrong = visual.GratingStim(win, color = [1,0,0], colorSpace = 'rgb', tex = None, mask = 'circle', units = 'cm', size = 0.2, pos = (0, 0)) # Paramters of FIXATION DOT continuously presented
fix_late = visual.GratingStim(win, color = [1,0,1], colorSpace = 'rgb', tex = None, mask = 'circle', units = 'cm', size = 0.2, pos = (0, 0)) # Paramters of FIXATION DOT continuously presented

# set both staircase counters to []
staircase_up, staircase_down = staircase_functions.reset_staircase_counters()  

# create timer
timer = core.Clock()

# create movement variables
movement_direction = 'no_change'
last_direction = 'not_set_yet'

# create and open log file to record parameter file, etc.

# create and open data file to record user output ADD TIMING OF EVERY TRIAL ETC
data_file = open('data_test.scdata', 'w') # o
data_file.write('Trial\tOrientation Counter\tOrientation Value\tResponse\tReversal Points Left\n')

# start trials
while number_reversals != 0 and number_trials != 0:  # ends when either is achieved

    # calculate grating orientation and create stimulus grating
    grating_ori, grating_dir = staircase_functions.calculate_grating_orientation(reference_ori, ori_list_created[ori_list_counter])
    grating = visual.GratingStim(win,contrast = 0.5, phase = 1, tex = 'sin', units = 'cm', mask = 'circle', sf = 2.4, size = 4, ori = grating_ori, pos=(4.5, 4.5))
    
    # present the stimulus 
    frame_counter = 0  # work with frames instead of time -> more accurate in psychopy
    while frame_counter != (win_fps*1.5): 
        fix_neutral.draw()
        grating.draw()
        win.flip()
        frame_counter += 1
    
    # obtain user feedback
    key_pressed = ''  # used to record last key pressed by user in underneath loop
    event.getKeys()  # clear all key presses
    frame_counter = 0
    while frame_counter != (win_fps*2) and key_pressed == '':  
        fix_neutral.draw()
        win.flip()
        all_keys_pressed = event.getKeys()
        if len(all_keys_pressed) != 0:
            key_pressed = all_keys_pressed[-1]  # only log the most recent key pressed
        frame_counter += 1
    
    # determine response type and show user feedback
    response = staircase_functions.calculate_response(key_pressed, grating_dir)  # returns 1 for correct, -1 for wrong and 0 for not responded or wrong key
    frame_counter = 0
    while frame_counter != (win_fps*1):
        if response == 1:
            fix_correct.draw()
        elif response == -1:
            fix_wrong.draw()
        elif response == 0:
            fix_late.draw()
        else:
            print('Error in feedback to user')
            core.quit()
        win.flip()
        frame_counter += 1
        
    # calculate staircase values
    staircase_up, staircase_down, movement_direction = staircase_functions.update_staircase_count(staircase_up, staircase_down, n_up, n_down, response)
    ori_list_counter = staircase_functions.calculate_orientation_list_counter(ori_list_counter, movement_direction, len(ori_list_created))
    number_reversals, movement_direction, last_direction = staircase_functions.calculate_number_reversals(number_reversals, movement_direction, last_direction)
    
    if response != 0:  # only "succesful" trial counter as trial
        number_trials -= 1
        
    trial_counter += 1
    data_file.write('{}\t{}\t{}\t{}\t{}\n'.format(trial_counter, ori_list_counter, ori_list_created[ori_list_counter], response, number_reversals))
