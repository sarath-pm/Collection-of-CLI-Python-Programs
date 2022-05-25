'''
Requirements

# pip install pyshorteners

'''

# Import module
from pyshorteners import Shortener

# Get the user input
url = input('Enter the URL:')

# Shorten the URL & print the output
shrinked = Shortener().clckru.short(url)
print('Shrinked URL:', shrinked)