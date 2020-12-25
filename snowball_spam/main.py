##############################################################################
#   Made by:     Kyle Hurd
#   Date:        12/24/2020
#   Description: Spams the snowball in CPR when a specific key-command is
#                pressed. End it by pressing another key-command specified
#                in the code below.
#
#                By default the START key-command is: r
#                By default the STOP  key-command is: e
#                By default the QUIT  key-command is: q
#
#
#   Dependencies:
#       - You need to pip install pynput
#       - The IDE may need permission to access keyboard and screen
#       - If you have multiple monitors, run the code on the secondary
#           and have the game on the primary monitor.
#
##############################################################################


# LIBRARIES
###########################
from pynput import keyboard, mouse
import threading


# FUNCTIONS
###########################
running = False
ms = mouse.Controller()
kb = keyboard.Controller()


def on_press(key):
    global running
    print(f'Key Pressed: {key}')
    if key.char == ('r') and running == False:
        running = True
        th1 = threading.Thread(target=spam)
        th1.start()
    elif key.char == ('e') and running == True:
        running = False
    elif key.char == ('q'):
        quit()
    return


def on_release(key):
    print(f'Key Released: {key}')
    return


def spam():
    global ms
    global kb
    global running
    
    while running:
        kb.type('T')
        ms.press(mouse.Button.left)
        ms.release(mouse.Button.left)
    return


def display_instructions():
    print('STOP:  e')
    print('START: r')
    print('QUIT:  q')
    return


display_instructions()

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
