rank_table = {
	'A': 1,
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'10': 10,
	'J': 11,
	'Q': 12,
	'K': 13,
}

def is_adjacent(rank1, rank2):
	delta = (rank1 - rank2) % 13
	return delta == 1 or delta == 12
