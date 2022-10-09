#!/usr/bin/env python3

import sys
if __name__ == '__main__':
	sys.stderr.write('Do not run from this script. Run main.py instead.')
	sys.exit(-1)

from solvers.common import *
from solvers import Pyramid
from solvers import TriPeaks

def solve(solitaire_type, fin, fout):
	type_f_dict = {
		'P': Pyramid.solve_Pyramid,
		'T': TriPeaks.solve_TriPeaks
	}
	return type_f_dict[solitaire_type](fin, fout)
