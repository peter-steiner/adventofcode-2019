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
    intcodeprg = [int(n) for n in readInput().split(',')]
    totsum = 0
    pos = 0    
    intcodeprg[1] = 12
    intcodeprg[2] = 2
    
    while intcodeprg[pos] != 99:
        #print("po: ", intcodeprg[pos])
        cmd = intcodeprg[pos]
        a = intcodeprg[intcodeprg[pos+1]]
        b = intcodeprg[intcodeprg[pos+2]]
        c = intcodeprg[pos+3]
        print("", a, b, c)
        if cmd == 1:
            print("1wtf", cmd)
            intcodeprg[c] = a + b
        if cmd == 2:
            print("2wtf", cmd)
            intcodeprg[c] = (a*b)
        pos += 4
        print("", intcodeprg)
    print("A): ", intcodeprg[0])

def b():
    rows = [n for n in readInput().split('\n')]
    totsum = 0

    print("B): ", totsum)

# Main body
if __name__ == '__main__':
    a()
    #Sb()
    sys.exit(1)
