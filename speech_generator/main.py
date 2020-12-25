##############################################################################
#   Made by:     Kyle Hurd
#   Date:        12/24/2020
#   Description: Reads a script from a given file, in which
#                each line in file is read and typed to screen
#                one at a time. The program automatically locates the text
#                box on the Club Penguin Rewritten site, but it
#                is important to not move the page up or down
#                as it only locates the chat box once (to save time).
#
#   Dependencies:
#       - You need to pip install cv2
#       - You need to pip install pyautogui
#       - The IDE may need permission to access keyboard and screen
#       - If you have multiple monitors, run the code on the secondary
#           and have the game on the primary monitor.
#
#       - The image of the chat bar must be pixel specific.
#           If program is not locating chat bar, consider taking a
#           screenshot of it yourself and placing it in images folder.
##############################################################################


# LIBRARIES
############################
import cv2
import pyautogui as py
import time as t


# FUNCTIONS
############################
    

# Waits a certain amount of time before beginning next line of code
def wait(seconds):
    t.sleep(seconds)
    return
  

def open_chrome_macos():
    wait(2)
    py.keyDown('command')
    py.keyDown('space')
    py.keyUp('space')
    py.keyUp('command')
    wait(2)
    py.press('delete')
    py.write('Google Chrome')
    wait(2)
    py.press('enter')
    wait(2)
    return
    
    
def open_chrome_win():
    py.press('win')
    py.write('Google Chrome')
    py.press('enter')
    return

# DRIVER
############################


# If you want to exit the program while it is running,
# move your cursor to the bottom left corner of the screen
# repeatedly. This will stop the program from running.

def main():

    # ALTERATIONS TO CODE
    #################################
    # Alter these items to change functionality of code
    
    
    wait_between_text = 5
    text_file_name = 'script.txt'
    image_name = 'chat_bar_4k.png'
    # For manual override if image cannot be found
    # chat_bar_x, chat_bar_y = 1020, 1070
    
    # CHANGE IF ON WINDOWS
    # open_chrome_win()
    # CHANGE IF ON MACOS
    open_chrome_macos()
    
    ##################################
    
    
    # Force exception
    py.useImageNotFoundException()
        
        
    # Getting dimensions of screen and chat bar location
    screen_width, screen_height = py.size()
       
       
    infile = open(text_file_name, 'r') # This file must be in the same directory as the .py file
    bad_words = '()[].+=-"' # These are the characters we dont want to include in our text
    
    
    # Start of Code
    ####################################
    
    
    for line in infile: # Going line by line in the infile
        for char in bad_words: # Filtering the line based on the 'bad_words'
            line = line.replace(char,'') # Replacing the 'bad_words' with ''
        
            # Getting Location of chat bar
        print('Finding chat bar on screen...')
        try:
            chat_bar_point = py.locateCenterOnScreen('./images/' + image_name)
        
        
            # YOU MAY HAVE TO COMMENT THIS IF YOU DO NOT HAVE 4K SCREEN
            #########################
            chat_bar_point_x = int(chat_bar_point.x / 2)
            chat_bar_point_y = int(chat_bar_point.y / 2)
            ########################
        
        
            # UNCOMMENT THIS IF IT DOESNT FIND CORRECT LOCATION
            ########################
            # chat_bar_point_y = chat_bar_point.y
            # chat_bar_point_x = chat_bar_point.x
            ########################
        
        
            print('Chat bar found')
        except py.ImageNotFoundException:
            print('ImageNotFoundException: chat bar not found')
            return
            
        py.click(chat_bar_point_x, chat_bar_point_y) # Clicks on the chat bar on CPR.
        py.click(chat_bar_point_x, chat_bar_point_y) # In case you clicked off program :)
        
                          
        py.write(line)    # Sends the filtered line as a keyboard input
        py.press('enter') # Presses return key. Displays to screen
        wait(wait_between_text) # Time between each cycle.
    
    
    # Ending program
    py.click(chat_bar_point_x, chat_bar_point_y)
    py.click(chat_bar_point_x, chat_bar_point_y)
    
    
    py.write('The end')
    py.press('enter')
    return


if __name__ == '__main__':
    main()
