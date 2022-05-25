'''
Requirements

# pip install pynput

'''

# Python Module
from pynput.mouse import Listener

# Function to print mouse position
def mouse_move(x,y):
    print("Mouse position is : ",format((x,y)))

# Listen mouse movement    
with Listener(on_move=mouse_move) as listener:
    listener.join()