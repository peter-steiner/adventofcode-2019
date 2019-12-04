#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2019/day/4
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d-4.test"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def solvePw(pwStr):
    pw = [int(c) for c in pwStr]
    valid = True
    adjacent = -1
    for i in range(len(pw)-1):
        if pw[i] > pw[i+1]:
            valid = False
            break
        if pw[i] == pw[i+1]:
            adjacent = pw[i]

    if adjacent < 0:
        valid = False
    return valid

def solvePwB(pwStr):
    pw = [int(c) for c in pwStr]
    valid = True
    adjacent = -1

    repeat = 0
    for i in range(len(pw)-1):
        if pw[i] > pw[i+1]:
            valid = False
        if pw[i] == pw[i+1]:
          c = pw.count(pw[i])
          pair_mod = pw.count(pw[i])%2
          if (pair_mod == 0 and c == 2):
            adjacent = pw[i]

    if adjacent < 0:
      valid = False

    return valid


def a():
    nmb_pws = 0    
    for pw in range(372037, 905157+1):
        if solvePw(str(pw)):
            nmb_pws += 1
    print("A): ", nmb_pws)

def b():
    nmb_pws = 0    
    for pw in range(372037, 905157+1):
        if solvePwB(str(pw)):
            nmb_pws += 1

    print("B): ", nmb_pws)

# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
