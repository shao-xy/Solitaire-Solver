#!/usr/bin/env python3

import sys
import os
import argparse
from solvers.common import *

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('input_path', help='Input file.')
  return parser.parse_args().input_path

def main():
  input_path = parse_args()
  counts = [0] * 13
  try:
    fin = open(input_path, 'r')
  except IOError as e:
    sys.stderr.write(str(e) + '\n')
    sys.stderr.flush()
    return e.errno

  ln = 0
  for line in fin.readlines():
    ln += 1
    items = line.strip().split()
    for item in items:
      if item not in rank_table:
        sys.stderr.write(f'Invalid card "{item}" in line {ln}\n')
        continue
      rank = rank_table[item]
      counts[rank - 1] += 1

  cards_ok = True
  for i in range(len(counts)):
    if counts[i] != 4:
      cards_ok = False
      rank_str = rank_str_table[i+1]
      sys.stderr.write(f'Error: There are {counts[i]} {rank_str} cards!\n')

  if cards_ok:
    sys.stdout.write('Perfect!\n')
      
  fin.close()
  return 0

if __name__ == '__main__':
  sys.exit(main())
