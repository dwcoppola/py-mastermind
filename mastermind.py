# 8, 10, or 12 guesses
import os
from random import random
from random import shuffle
def get_code(colors, blanks, dupes):
    rand = 6
    color_list = ["red", "yellow", "green", "blue", "black", "white"]
    shuffle(color_list)
    if colors >= 7:
        rand += 1
        color_list.append("orange")
        shuffle(color_list)
        if colors == 8:
            rand += 1
            color_list.append("purple")
            shuffle(color_list)
    if blanks == True:
        rand += 1
        color_list.append("blank")
        shuffle(color_list)
    new_list = []
    if dupes == True:
        while len(new_list) < 4:
            new_list.append(color_list[int(random() * rand)])
    else: 
        while len(new_list) < 4:
            color = color_list[int(random() * rand)]
            if color in new_list:
                continue
            else:
                new_list.append(color)
    return new_list
def victory_fanfare():
    print("You win!")
    return True
def give_feedback(code, guess):
    white = red = blank = 0
    i = 0 
    for v in guess:
        if v == code[i]:
            red += 1
        i += 1
    for v in guess:
        if code.count(v) > 0:
            white += 1
    white = white - red
    blank = 4 - white - red
    feedback = [red, white, blank]
    final_feedback = []
    for v in range(feedback[0]):
        final_feedback.append("red")
    for v in range(feedback[1]):
        final_feedback.append("white")
    for v in range(feedback[2]):
        final_feedback.append("blank")
    return final_feedback
def get_acceptable_responses(colors, blanks):
    if colors == 6:
        acceptable = ["red", "yellow", "green", "blue", "black", "white"]
        if blanks == True:
            acceptable.append("blank")
    elif colors == 7:
        acceptable = ["red", "orange", "yellow", "green", "blue", "black", "white"]
        if blanks == True:
            acceptable.append("blank")
    elif colors == 8:
        acceptable = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]
        if blanks == True:
            acceptable.append("blank")   
    return acceptable
while True:
    os.system("cls")
    answer = input("""WELCOME TO MASTERMIND

    Please choose from the following options:

    1. Help / Instructions
    2. Play As Codebreaker
    3. Quit

    """)
    if answer == "1":
        pass
    elif answer == "2":
        os.system("cls")
        turns = input(""""How many turns would you like the match to be? 
(Choose 8, 10, or 12 -- Default is 8) """)
        # set the number of guesses
        if turns == "8" or turns == "10" or turns == "12":
            turns = int(turns)
        else:
            turns = 8
        # set the number of colors
        colors = input("""Next select how many colors to use. 
You can choose 6, 7, or 8 colors (default is 6): """)
        if colors == "6" or colors == "7" or colors == "8":
            colors = int(colors)
        else:
            colors = 6
        # set whether or not duplicate colors can be in the code
        dupes = input("""You can choose if duplicate colors are allowed.
The default is no. Please answer Y/N to duplicate colors: """)
        if dupes.lower() == "y" or dupes.lower() == "yes":
            dupes = True
        else:
            dupes = False
        # set whether 'blank' is an acceptable value
        blanks = input("""Lastly, you can choose if blank slots are allowed.
The default is no. Please answer Y/N to blank slots: """)
        if blanks.lower() == "y" or blanks.lower() == "yes":
            blanks = True
        else:
            blanks = False
        acceptable = get_acceptable_responses(colors, blanks) # assign acceptable guesses to a variable
        secret_code = get_code(colors, blanks, dupes) # this generates the secret code
        os.system("cls")
        while True:
            print(f"You have {turns} guesses remaining")
            print()
            guess = input("What is your guess? ").split(",")
            clean_guess = []
            for v in guess:
                clean_guess.append(v.strip())
            guess = clean_guess
            print(give_feedback(secret_code, guess))
            turns -= 1
            if give_feedback(secret_code, guess) == ["red", "red", "red", "red"]:
                input("You win! Press 'Enter'!")
                break
            elif turns == 0:
                print("You lose!")
                print(f"The answer was {secret_code}!")
                input("Press 'Enter'.")
                break
            else:
                input("Press 'Enter' when you're ready to guess again.")
                continue
    elif answer == "3":
        break
    else:
        continue