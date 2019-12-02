#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2018/day/1
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d-1"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def cFuel(mass):
    return math.floor(float(mass)/3)-2

def bcFuel(mass):
    totfuel = 0
    newmass = mass
    while newmass != 0:
        newmass = cFuel(newmass)
        #print("newmass: ", newmass)
        if newmass < 0:
            newmass = 0
        totfuel += newmass 
    return totfuel

def a():
    rows = [n for n in readInput().split('\n')]
    totsum = 0
    for row in rows:
        fuel = cFuel(row)
        #print("input:", fuel)
        totsum += fuel
    print("A): ", totsum)

def b():
    rows = [n for n in readInput().split('\n')]
    totsum = 0
    for row in rows:
        fuel = bcFuel(float(row))
        totsum += fuel
        #print("input:", fuel)
    print("B): ", totsum)

# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
