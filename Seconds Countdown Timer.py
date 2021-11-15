# Countdown Timer by Seconds
# User input total time in H, M and S. then returns total time and count down

import time


def countdown():  # user input and print instructions
    h_time = float(input('Enter hours: '))
    if h_time > 0:  # question why so long
        question = input('Do you really want to wait 3600 seconds??? (Y or N) ').lower()  # ask user yes or no
        if question == 'n':  # if user says no then set h_time to 0
            h_time = 0

    m_time = float(input('Enter minutes: '))
    hours = round(h_time * 3600, 5)  # convert to sec
    minutes = round(m_time * 60, 5)  # convert to sec
    seconds = hours + minutes
    print('There are ' + str(seconds) + ' seconds in ' + str(h_time) + ' hours and ' + str(m_time) + ' minutes.')

    while seconds >= 0:  # loop for countdown
        # '{:0.2f}'.format(seconds)  will format to 2 decimal. print will use 0
        print(str('{:0.0f}'.format(seconds)) + ' Seconds Left')
        seconds = seconds - 1
        time.sleep(1)
        if seconds == 15:  # warning
            print('Getting Close to Finish!')
        elif seconds == 10:
            print('DANGER much close!')
        elif seconds == 5:
            print('Ruh Roh, V close!')
        elif seconds == 3:
            print('Here Weeeee GOOOO!')

    print('BUZZ BUZZZZ!!! TIME IS UP!!!')


countdown()
