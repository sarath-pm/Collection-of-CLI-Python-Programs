# import necessary py modules
import random
import time

# variables
computerwins = 0
playerwins = 0
ties = 0
end = 0

# looping the game 
while True:
    choices = ["stone", "paper", "scissors"]

    # getting user input
    user_choice = input("'stone', 'paper', 'scissors', or 'end': ")

    # print randomized computer output
    computer_choice = (random.choice(choices))
    print(computer_choice)

    # compare user & computer & output the result
    if user_choice == computer_choice:
        time.sleep(0.5)
        print("Tie!\n")
        ties += 1
        end += 1

    elif user_choice == "stone":
        if computer_choice == "paper":
            time.sleep(0.5)
            print("Computer Win!\n")
            computerwins +=1
            end += 1

        else:
            time.sleep(0.5)
            print("Player win!\n")
            playerwins += 1
            end += 1

    elif user_choice == "paper":
        if computer_choice == "stone":
            time.sleep(0.5)
            print("Player win!\n")
            playerwins += 1
            end += 1

        else:
            time.sleep(0.5)
            print("Computer win!\n")
            computerwins += 1
            end += 1

    elif user_choice == "scissors":
        if computer_choice == "stone":
            time.sleep(0.5)
            print("Computer win!\n")
            computerwins += 1
            end += 1

        else:
            time.sleep(0.5)
            print("Player win!\n")
            playerwins += 1
            end += 1

    # End the game and dispaly the final scores
    elif user_choice == "end":
            choices.append("end")
            print("\nWonderful game!\nYour final scores:\n") 
            print("Total score for Player: ", playerwins, "wins!")
            print("Total score for Computer: ", computerwins, "wins!")
            print("Total ties: ", ties, "ties!")
            break