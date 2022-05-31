'''
Run the script as Administrator

'''

# import necessary py modules
from datetime import datetime

# select block or unblock site
user_input = input('Select \"1\" to block or \"2\" to unblock sites: ')

# lists of website to block
sites_to_block = ['www.facebook.com', 'facebook.com']

# hosts_path = '/etc/hosts' # Path for linux os
hosts_path = r"C:\Windows\System32\drivers\etc\hosts" # Path for windows os

# redirect the website to another website or local host 
redirect = "127.0.0.1" # local host IP 

# function to block website
def block_websites():
    print("Block sites")
    with open(hosts_path, 'r+') as hostfile:
        hosts_content = hostfile.read()
        for site in  sites_to_block:
            if site not in hosts_content:
                hostfile.write(redirect + ' ' + site + '\n')

# function to unblock websites
def unblock_websites():
    print('Unblock sites')
    with open(hosts_path, 'r+') as hostfile:
        lines = hostfile.readlines()
        hostfile.seek(0)
        for line in lines:
            if not any(site in line for site in sites_to_block):
                hostfile.write(line)
        hostfile.truncate()

# call functions 
if user_input == '1':
    block_websites()
elif user_input == '2':
    unblock_websites()
else:
    print('Invalid Input. Try again!')
