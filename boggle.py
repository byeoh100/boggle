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
			new_row_list = [self.dice_picker_roller() for x in range(4)]
			new_row = ""
			for i in new_row_list: # Maybe put this in it's own formatting method
				if i == "Q":
					new_row += f"Qu "
				else:
					new_row += f"{i}  "
			self._board_list.append(new_row_list)
			new_board.append(new_row.strip())

		self._board = new_board

	def dice_picker_roller(self):
		dice_num = random.randrange(0, len(self._dice))
		picked_dice = self._dice[dice_num]
		picked_letter = picked_dice[random.randrange(0, 6)]

		self._dice.pop(dice_num)
		return picked_letter
	
	def word_checker(self, word):
		for i in word:
			if not any(i in x for x in self._board_list):
				return False
		word_start_list =drffd [[j for i in range(len(i)) for j in range(len(self._board_list))]]
		return word_start_list

def print_board():
	for i in board1.board:
		print(i)

board1 = BoggleBoard()
board1.shake()
print_board()
#word = input("Enter word: ")
print(board1.word_checker("A"))