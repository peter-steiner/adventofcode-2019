#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2019/day/10
"""

# Imports
import sys
import os
import re
import math
import time
import itertools

# Global variables
#task="d-10.test"
task="d-10"
infile=task

def readInput(test):
    with open('input/' + infile + test + '.input') as file:
        data = file.read()
    file.close()
    return data


def test():
  print("Test run")

def readSpace(rows):

  space = []
  for row in rows:
    r = []
    for c in row:
      if  c == '#':
        r.append(1)
      else: 
        r.append(0)
    space.append(r)

  return space

# x, y
def getLimits(space):
  return [len(space[0])-1, len(space)-1]

def printSpace(space):
  for room in space:
    print(room)

def validPoint(point, limits):
  x, y = point
  if x >= 0 and x <= limits[0]:
    return True
  if y >= 0 and y <= limits[1]:
    return False

def a():
  rows = [n for n in readInput(".test").split('\n')]

  space = readSpace(rows)
  printSpace(space)
  limits = getLimits(space)


  print("A): ")

def b():
  instruction = [int(n) for n in readInput().split(',')]

  print("B): ", instruction)

# Main body
if __name__ == '__main__':
    # test()
    a()
    # b()
    sys.exit(1)
