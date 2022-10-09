#!/usr/bin/env python3
# vim: noexpandtab

import sys
import argparse
from solvers import solver

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('type', choices=['P', 'T'], help='Solitaire type.')
	parser.add_argument('-i', '--input', help='Read data from input file instead of stdin.')
	parser.add_argument('-o', '--output', help='Write data to input file instead of stdout.')
	return parser.parse_args()

def main():
	args = parse_args()
	fin = args.input and open(args.input, 'r') or sys.stdin
	fout = args.output and open(args.output, 'w') or sys.stdout

	return solver.solve(args.type, fin, fout)

if __name__ == '__main__':
	sys.exit(main())
