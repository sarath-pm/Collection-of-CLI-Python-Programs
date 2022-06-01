'''
Requirements

# pip install zipfile
'''
# importing required modules
from lzma import FILTER_SPARC
from zipfile import ZipFile
import os

# get the user input to proceed
user_input = input("Select 1 to zip or 2 to unzip: ")

# loop the script if it's a invalid input
while user_input not in {"1", "2"}:
    user_input = input("Invalid Input. Select the correct Input.\nSelect 1 to zip or 2 to unzip: ")

# get path from user
directory = input("Enter Directory Path: ")


# fucntion to get all the file paths
def get_all_file_paths(directory):

    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, _directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths		

class Zip_Unzip:
    # function to zip
    def zip():

        # calling function to get all file paths in the directory
        file_paths = get_all_file_paths(directory)

        # printing the list of all files to be zipped
        print('Following files will be zipped:\n')
        for file_name in file_paths:
            print(file_name)

        # writing files to a zipfile
        with ZipFile('zipped_files.zip','w') as zip:
            # writing each file one by one
            for file in file_paths:
                zip.write(file)

        print('\nAll the files are zipped successfully...!!!')		

    # function to unzip 
    def unzip():
        # path to folder which need to be unzipped
        #directory = input("Enter the file path to unzip: ")
        with ZipFile(directory,"r") as unzipping:
            unzipping.extractall()

        print('Successfully unzipped all the files..!!!')


# selecting class functions to execute
if user_input == '1':
    Zip_Unzip.zip()
elif user_input == '2':
    Zip_Unzip.unzip()
else: 
    pass
