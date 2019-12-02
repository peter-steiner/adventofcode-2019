#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2019/day/1
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d-2"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [n for n in readInput().split('\n')]
    totsum = 0
    for row in rows:
        print("row: ", row)

    print("A): ", totsum)

def b():
    rows = [n for n in readInput().split('\n')]
    totsum = 0

    print("B): ", totsum)

# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
