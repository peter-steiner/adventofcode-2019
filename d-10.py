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
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data


def test():
  print("Test run")

def a():
  instruction = [int(n) for n in readInput().split(',')]

  print("A): ", instruction)

def b():
  instruction = [int(n) for n in readInput().split(',')]

  print("B): ", instruction)

# Main body
if __name__ == '__main__':
    # test()
    a()
    b()
    sys.exit(1)
