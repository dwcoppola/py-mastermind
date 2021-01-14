# 8, 10, or 12 guesses

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
    print("You win")

def analyze_guess(code, guess):
    feedback = []