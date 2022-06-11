# import necessary py modules
import random

# hangman images 
hangmanimg = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# list of words to guess
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

# Function returns a random string from the passed list of strings.
def get_random_word(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

def display_img(hangmanimg, wrong_guess, correct_letters, secret_word):
    print(hangmanimg[len(wrong_guess)])
    print()
    print('Wrong guess letters:', end=' ')
    for letter in wrong_guess:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)): # replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

# Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
def get_input(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

# Function returns True if the player wants to play again, otherwise it returns False.
def play_again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
wrong_guess = ''
correct_letters = ''
secret_word = get_random_word(words)
gameIsDone = False

while True:
    display_img(hangmanimg, wrong_guess, correct_letters, secret_word)
    # Let the player type in a letter.
    guess = get_input(wrong_guess + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess
        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secret_word + '"! You have won!')
            gameIsDone = True
    else:
        wrong_guess = wrong_guess + guess
        # Check if player has guessed too many times and lost
        if len(wrong_guess) == len(hangmanimg) - 1:
            display_img(hangmanimg, wrong_guess, correct_letters, secret_word)
            print('You have run out of guesses!\nAfter ' + str(len(wrong_guess)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "' + secret_word + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if play_again():
            wrong_guess = ''
            correct_letters = ''
            gameIsDone = False
            secret_word = get_random_word(words)
        else:
            break