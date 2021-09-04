"""
File: hangman.py
Name: Jeff
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7
logo = """
  _                                             
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    |___/                                             
"""
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
      |
      |
      |
      |
      |
=========
''']

def main():
    """
    A game which players have to guess the word, players can input a guess alphabet
    each round, and will tell players whether the guess is correct and will show
    the updated word on console, each player have N_TURNS chances to answer wrong
    """
    print(logo)
    answer = random_word()
    guess = ''
    for i in range(len(answer)):
        guess += '_'
    life = N_TURNS
    while life > 0:
        print(stages[life])
        print("The word looks like: " + guess)
        print("You have " + str(life) + " gusses left")
        guess_string = input("Your guess: ")
        while True:  # if the input is not accepted, it will print illegal format and ask layers to input new guess
            if not guess_string.isalpha():
                print(stages[life])
                print("illegal format")
                guess_string = input("Your guess: ")
            elif len(guess_string) > 1:
                print(stages[life])
                print("illegal format")
                guess_string = input("Your guess: ")
            else:
                break

        guess_string = guess_string.upper()
        for i in range(len(answer)):
            if guess_string == answer[i]:
                x = ''
                x += guess
                guess = ''
                for j in range(len(answer)):  # combine the new guess based on the updated guess
                    if i != j:
                        guess += x[j]
                    else:
                        guess += guess_string
                print(stages[life])
                print("You are correct!")
        if guess_string not in answer:  # if the guess is wrong, players will lost one turn
            life -= 1
            print(stages[life])
            print("There is no " + guess_string + "'s in the word.")

        if life == 0:  # if the turns reduced to zero, player lost the game
            print(stages[life])
            print("You are completely hung : ( ")
            print("The word was: " + answer)
        if guess == answer:  # if the player guess the word correctly , player win the game
            print(stages[life])
            print("You win!")
            print("The word was: " + answer)
            life = 0


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
