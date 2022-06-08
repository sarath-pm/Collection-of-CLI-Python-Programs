# import necessary py modules
import random
import string

# get random string of letters, digits and special characters
merge = string.ascii_letters + string.digits + string.punctuation

# get the user_input 
user_input = input('Enter the length of the password to be generated: ')

# join and generate a password
generated_passwd = ''.join((random.choice(merge) for i in range(int(user_input))))

# print the generated password
print(generated_passwd)