'''
Requirements

# pip install beautifulsoup
#pip install requests

'''

# import necessary py modules
from bs4 import BeautifulSoup
import requests

#  setting user agent
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# function to get weather of the city
def weather(city):
	city = city.replace(" ", "+")
    # get the information from the web 
	res = requests.get(
		f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
	print("Looking for the weather info over the web....\n")
    # parse the information from the webpage 
	soup = BeautifulSoup(res.text, 'html.parser')
	location = soup.select('#wob_loc')[0].getText().strip()
	time = soup.select('#wob_dts')[0].getText().strip()
	info = soup.select('#wob_dc')[0].getText().strip()
	weather = soup.select('#wob_tm')[0].getText().strip()
    # output the retrived info
	print(location)
	print(time)
	print(info)
	print(weather+"°C")

# get user input
city = input("Enter the name of the City: ")
city = city+" weather"
weather(city)