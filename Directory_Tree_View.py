# import necessary py modules
import os

# Calling the function in this class
class Tree_view:
    
   # Function to generate dir tree
   def generate( self, path ):
       if os.path.exists(path):
          for root, dirs, files in os.walk(path):
              folder = root.replace(path,'')
              Count = folder.count(os.sep)
        
              spaces = ' '*3*Count
        
              print(f'{spaces}🖿  {os.path.basename(root)}/')
        
              for file in files:
                  sub_space = ' '*4
                  print(f'{spaces}{sub_space}➥  {file}')

       # Error output if file not found           
       else:
          print(f'\"{path}\" --> No such file or directory found..!')

# Call the class and get user input
user_input = Tree_view()
user_input.generate(input('Enter Directory path: '))              