# import necessart py modules
import os

# get user input
folder = input(r'Enter the folder name to remane: ') 
rename_as = input('Enter the name to rename: ')
extension = input("Enter the files extension to rename: ")

count = 1
# count increase by 1 in each iteration
# iterate all files from a directory
for file_name in os.listdir(folder):
    # Construct old file name
    source = folder + file_name

    # Adding the count to the new file name and extension
    destination = folder + rename_as + str(count) + extension

    # Renaming the file
    os.rename(source, destination)
    count += 1
print('All Files Renamed')


# verify the result
res = os.listdir(folder)
print('New Names are:\n', res)