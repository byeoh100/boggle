from boggle import Color, BoggleBoard
import os
import time

board = BoggleBoard()
found_words = []

def start():
    os.system("cls||clear")
    board.shake()

def game_loop(): # Could use some re-org
    os.system("cls||clear")
    board.print
    print("Found words: {}".format(found_words))
    print("s to shake | 0 to quit")
    word = input("Enter word: ").lower()

    if word == "0":
        return word
    elif word == "s":
        return 2
    elif word not in open("wordlist.txt").read():
        print(Color.RED + "Not a word" + Color.END)
        time.sleep(1)
        return -1
    elif word.upper() in found_words:
        print(Color.RED + "Word used" + Color.END)
        time.sleep(1)
        return -1
    
    found_or_not = board.first_letter_finder(word.upper())

    if found_or_not == "Word not found!":
        print(Color.RED + found_or_not + Color.END)
    else:
        found_words.append(word.upper())
        print(Color.GREEN + found_or_not + Color.END)
    time.sleep(1)

selection = input("p to play | 0 to quit\n")
start()
while selection != "0":
    if selection == 2:
        start()
        found_words = []
    selection = game_loop()

os.system("cls||clear")
print("Goodbye")