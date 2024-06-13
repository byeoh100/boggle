import random

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

	@property
	def board(self):
		return self._board

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
	
	def first_letter_finder(self, word):
		first_letters = []
		
		for row_i, row in enumerate(self._board_list):
			if word[0] in row:
				col_i = row.index(word[0])
				first_letters.append([row_i, col_i])

		result = self.word_checker(word, first_letters)
		return result

	def word_checker(self, word, first_letters):
		next_letter_i = 0

		for i in first_letters:
			row_i = [i[0]]
			col_i = [i[1]]
			path = []
			path.append([row_i, col_i])
			next_letter_i += 1
			used_i = []

			while len(path) > 0:
				if next_letter_i == len(word):
					return path
				last_ele = path[-1] # error here
				path_head_row = last_ele[0]
				path_head_col = last_ele[1]
				search = self.check_sides(word[next_letter_i], path_head_row, path_head_col, used_i)
				if search == -1:
					used_i.append([path_head_row, path_head_col])
					path.pop()
					next_letter_i -= 1
				else:
					path.append(search)
					next_letter_i += 1
			
			return -1
	
	def check_sides(self, next_letter, row_i, col_i, used_i):
		for row in range(-1, 2):
			for col in range(-1, 2):
				new_row_i = row_i + row
				new_col_i = col_i + col
				x_bound = len(self._board_list) - 1
				y_bound = len(self._board_list[row_i]) - 1
				
				if new_row_i > x_bound or new_row_i < 0 or new_col_i > y_bound or new_col_i < 0 or row == 0 and col == 0 or [new_row_i, new_col_i] in used_i:
					continue
				if self._board_list[new_row_i][new_col_i] == next_letter:
					return [new_row_i, new_col_i]
		
		return -1

def print_board():
	for i in board1.board:
		print(i)

board1 = BoggleBoard()
board1.shake()
print_board()
word = input("Enter word: ")
print(board1.first_letter_finder(word.upper()))
pass