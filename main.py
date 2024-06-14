from boggle import Color, BoggleBoard
import os
import time

board = BoggleBoard()

def start():
    os.system("cls||clear")
    board.shake()

def game_loop():
    os.system("cls||clear")
    board.print
    word = input("Enter word: ")
    if word == "0":
        return word
    found_or_not = board.first_letter_finder(word.upper())
    if found_or_not == "Word not found!":
        print(Color.RED + found_or_not + Color.END)
    else:
        print(Color.GREEN + found_or_not + Color.END)
    time.sleep(1)

selection = input("p to play | 0 to quit\n")
start()
while selection != "0":
    selection = game_loop()

os.system("cls||clear")
print("Goodbye")