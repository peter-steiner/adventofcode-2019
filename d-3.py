#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2019/day/3
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d-3"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    inp = [int(n) for n in readInput().split(',')]        

    print("A): ", inp)

def b():
    inp = [int(n) for n in readInput().split(',')]        

    print("B): ", inp)


# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
