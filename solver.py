#!/usr/bin/env python3

import sys
if __name__ == '__main__':
	sys.stderr.write('Do not run from this script. Run main.py instead.')
	sys.exit(-1)

from topo import TriPeaksTopo
from common import *

def solve_TriPeaks(deck, cards, topo, available_positions, actions, deck_pos, cur_rank):
	if not available_positions:
		# Solved: no cards left
		return actions, True
	if deck_pos > 23:
		# Unsolved
		#sys.stderr.write('Unsolved!\n')
		return None, False

	zipped_available_positions = zip(range(len(available_positions)), available_positions)
	possible_positions = [ t for t in list(zipped_available_positions) if is_adjacent(cards[t[1]], cur_rank) ]

	for idx, pos in possible_positions:
		new_available_positions = available_positions.copy() + topo.pick(pos)
		del new_available_positions[idx]
		action_list, ret = solve_TriPeaks(deck, cards, topo, new_available_positions, actions + [pos], deck_pos, cards[pos])
		if ret:
			return action_list, ret
		topo.unpick(pos)

	# Empty or all failed?
	return solve_TriPeaks(deck, cards, topo, available_positions, actions + [-1], deck_pos + 1, deck[deck_pos+1])

def solve(fin, fout):
	deck, cards = TriPeaksTopo.load_challenge(fin)
	action_list, ret = solve_TriPeaks(deck, cards, TriPeaksTopo(), list(range(10)), [], 0, deck[0])
	if ret < 0:	return ret
	
	for action in action_list:
		fout.write('%s\n', str(action))
	fout.close()
	return 0
