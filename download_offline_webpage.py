'''
Requirements

# pip install pywebcopy

'''

# import necessary py modules
import pywebcopy

# get user input
user_input = input("1) To download single wepage\n2) To download full webiste\nSelect 1 or 2: ")
url = input("Enter the URL to download: ")
download_folder = input('Enter folder path to download: ''')

# options to download using pywebcopy module
kwargs = {'bypass_robots': True, 'debug': False, 'open_in_browser': True, 'delay': None, 'threaded': False}

# execute the program as per user_input
if user_input == '1':
    pywebcopy.save_webpage(url, download_folder, **kwargs, project_name='single_webpage')
if user_input =='2':
    pywebcopy.save_website(url, download_folder, **kwargs, project_name='full_website')
else:
    print("Invalid Input")