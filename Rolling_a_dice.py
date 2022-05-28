# import necessary py modules
import random

# variable to run or exit the program
run = 1
level = 0

# Looping the code for rolling the dice
while(run == 1):
        print("**ROUND " + str(level) + "**") 
        print("player 1: ",random.randint(0, 6))
        print("player 2: ",random.randint(0, 6)) # you can comment/remove it if your are playing alone or add more player's as you wish
        run = int(input("\nEnter ""1"" to go again or ""0"" to end: "))
        print("")
        level += 1