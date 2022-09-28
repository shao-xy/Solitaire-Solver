from common import *

class Cell:
	def __init__(self, pos):
		self.pos = pos
		self.parents = []
		self.children = []
		self.used = False
	
	def available(self):
		if self.used:	return False
		for parent in self.parent:
			if not parent.used:
				return False
		return True

	def pick(self):
		assert(self.available())
		self.used = True
		return [child.pos for child in self.children if child.available()]

	def unpick(self):
		for child in self.children:
			assert(not child.used)
		self.used = False

	@staticmethod
	def link_child(parent_cell, child_cell):
		parent_cell.children.append(child_cell)
		child_cell.parents.append(parent_cell)

class TriPeaksTopo:
	def __init__(self):
		cells = []
		for i in range(28):
			cells.append(Cell(i))

		# First line
		Cell.link_child(cells[0], cells[10])
		Cell.link_child(cells[1], cells[10])
		Cell.link_child(cells[1], cells[11])
		Cell.link_child(cells[2], cells[11])
		Cell.link_child(cells[2], cells[12])
		Cell.link_child(cells[3], cells[12])
		Cell.link_child(cells[3], cells[13])
		Cell.link_child(cells[4], cells[13])
		Cell.link_child(cells[4], cells[14])
		Cell.link_child(cells[5], cells[14])
		Cell.link_child(cells[5], cells[15])
		Cell.link_child(cells[6], cells[15])
		Cell.link_child(cells[6], cells[16])
		Cell.link_child(cells[7], cells[16])
		Cell.link_child(cells[7], cells[17])
		Cell.link_child(cells[8], cells[17])
		Cell.link_child(cells[8], cells[18])
		Cell.link_child(cells[9], cells[18])

		# Second line (Peak 1)
		Cell.link_child(cells[10], cells[19])
		Cell.link_child(cells[11], cells[19])
		Cell.link_child(cells[11], cells[20])
		Cell.link_child(cells[12], cells[20])

		# Second line (Peak 2)
		Cell.link_child(cells[13], cells[21])
		Cell.link_child(cells[14], cells[21])
		Cell.link_child(cells[14], cells[22])
		Cell.link_child(cells[15], cells[22])

		# Second line (Peak 3)
		Cell.link_child(cells[16], cells[23])
		Cell.link_child(cells[17], cells[23])
		Cell.link_child(cells[17], cells[24])
		Cell.link_child(cells[18], cells[24])

		# Third line (Peaks 1-3)
		Cell.link_child(cells[19], cells[25])
		Cell.link_child(cells[20], cells[25])
		Cell.link_child(cells[21], cells[26])
		Cell.link_child(cells[22], cells[26])
		Cell.link_child(cells[23], cells[27])
		Cell.link_child(cells[24], cells[27])

	def pick(self, pos):
		cell = self.cells[pos]
		return cell.pick()

	def unpick(self, pos):
		cell = self.cells[pos]
		return cells.unpick()

	@staticmethod
	def load_challenge(fin):
		def read_card_list(fin):
			cardlist_strs = fin.readline().strip().split()
			cardlist = [ rank_table[s] for s in cardlist_strs if s ]
			return cardlist

		# First line: the deck
		deck = read_card_list(fin)
		assert(len(deck) == 24)

		# Next lines: cards 0-9, 10-18, 19-24, 25-27
		cards = []
		for i in range(3):
			cards += read_card_list(fin)
		assert(len(cards) == 28)

		fin.close()
		
		return deck, cards
