from solvers.common import *

class Cell:
	def __init__(self, pos):
		self.pos = pos
		self.parents = []
		self.children = []
		self.used = False
	
	def available(self):
		if self.used:	return False
		for parent in self.parents:
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

