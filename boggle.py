import random
import time
import os

class Color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

class BoggleBoard:
	master_dice = ["AAEEGN", "ELRTTY" ,"AOOTTW", "ABBJOO", "EHRTVW", "CIMOTU", "DISTTY", "EIOSST", "DELRVY", "ACHOPS", "HIMNQU", "EEINSU", "EEGHNW", "AFFKPS", "HLNNRZ" ,"DEILRX"]

	def __init__(self):
		self._board = [
			"_  _  _  _",
			"_  _  _  _",
			"_  _  _  _",
			"_  _  _  _"
		]
		self._board_list = []
		self._dice = [x for x in BoggleBoard.master_dice]
		self._path_dict = {}

	@property
	def print(self):
		for i in self._board:
			print(i)

	def shake(self):
		new_board = []

		for i in range(4):
			new_row_i_list = [self.dice_picker_roller() for x in range(4)]
			new_row_i = ""
			for i in new_row_i_list: # Maybe put this in it's own formatting method
				if i == "Q":
					new_row_i += f"Qu "
				else:
					new_row_i += f"{i}  "
			self._board_list.append(new_row_i_list)
			new_board.append(new_row_i.strip())

		self._board = new_board

	def dice_picker_roller(self):
		dice_num = random.randrange(0, len(self._dice))
		picked_dice = self._dice[dice_num]
		picked_letter = picked_dice[random.randrange(0, 6)]

		self._dice.pop(dice_num)
		return picked_letter
	
	def first_letter_finder(self, word): # Q is an invalid input
		first_letters = []
		
		for row_i, row in enumerate(self._board_list):
			for col_i, col in enumerate(row):
				if col == word[0]:
					first_letters.append((row_i, col_i))

		result = self.word_checker(word, first_letters)
		
		if result == -1:
			return "Word not found!"
		self.highlight_word(result)
		return "Word found!"

	def word_checker(self, word, first_letters): # still looping back
		for start_i in first_letters:
			path = [start_i]
			next_letter_i = 1
			debug = 0

			while len(path) > 0:
				if next_letter_i == len(word):
					return path
				
				self.set_path_dict(path[-1], path[-1])
				used_i = self.get_path_dict(path[-1])
				path_head_row, path_head_col = path[-1]
				search = self.check_sides(word[next_letter_i], path_head_row, path_head_col, used_i)
				
				if search == -1:
					path.pop()
					next_letter_i -= 1
				else:
					self.set_path_dict(path[-1], search)
					path.append(search)
					next_letter_i += 1
				
				debug += 1
				if debug == 15:
					print(path, word[next_letter_i], used_i)
					break
			
			used_i.clear()
			
		return -1
	
	def check_sides(self, next_letter, row_i, col_i, used_i):
		for row in range(-1, 2):
			for col in range(-1, 2):
				if row == 0 and col == 0:
					continue

				new_row_i = row_i + row
				new_col_i = col_i + col
				x_bound = len(self._board_list) - 1
				y_bound = len(self._board_list[row_i]) - 1
				
				if new_row_i > x_bound or new_row_i < 0 or new_col_i > y_bound or new_col_i < 0 or (new_row_i, new_col_i) in used_i:
					continue
				if self._board_list[new_row_i][new_col_i] == next_letter:
					return (new_row_i, new_col_i)
		
		return -1
	
	def get_path_dict(self, coords):
		return self._path_dict[coords]
	
	def set_path_dict(self, curr_pos, dead_end):
		if curr_pos in self._path_dict and self._path_dict[curr_pos] == dead_end:
			return 0
		elif curr_pos in self._path_dict:
			self._path_dict[curr_pos].append(dead_end)
		else:
			self._path_dict[curr_pos] = [dead_end]
	
	def highlight_word(self, letter_list_i):
		print_list = []
		for i in range(len(letter_list_i)):
			os.system("cls||clear")
			print_list.append(letter_list_i[i])
			for row_i, row in enumerate(self._board_list):
				for col_i, col in enumerate(row):
					coords = (row_i, col_i)
					if coords in print_list:
						print(Color.BLUE + col + Color.END, end = "")
					else:
						print(col, end="")
					
					if col_i == len(row) - 1:
						print()
					else:
						print("  ", end="")
			
			time.sleep(0.5)

# board1 = BoggleBoard()
# board1.shake()
# board1.print
# word = input("Enter word: ")
# print(board1.first_letter_finder(word.upper()))

# items to add
# used word list
# valid word list
# timer