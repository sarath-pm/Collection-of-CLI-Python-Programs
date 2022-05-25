'''
Requirements

# pip install requesrs
# pip install bs4

'''

# Python Modules
import requests
from bs4 import BeautifulSoup
 
# get URL from the user
url = input('Enter URL:')
grab = requests.get(url)
soup = BeautifulSoup(grab.text, 'html.parser')
 
# opening a file in write mode
file = open("extracted_urls.txt", "w")

# traverse paragraphs from soup
for link in soup.find_all("a"):
   data = link.get('href')
   print(data)
   file.write(data)
   file.write("\n")

file.close()