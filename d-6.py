#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2019/day/6
"""

# Imports
import sys
import os
import re
import math
import time

# Global variables
# task="d-6.test"
task="d-6"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    instructions = [int(n) for n in readInput().split(',')]        
    answ = ""    
    print("A): ", answ)

def b():
    instructions = [int(n) for n in readInput().split(',')]        
    answ = ""    
    print("B): ", answ)

# Main body
if __name__ == '__main__':
    # test()
    a()
    b()
    sys.exit(1)
