#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2019/day/5
"""

# Imports
import sys
import os
import re
import math

# Global variables
# task="d-5.test"
task="d-5"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def getOutput(instruction):
    pos = 0
    input = 1
    while instruction[pos] != 99:
        cmd = [int(d) for d in str(instruction[pos])]

        # Hantera 
        # ABCDE
        #  1002
        if len(cmd) > 1:
            A = 0
            l = len(cmd)
            if l > 4:
                print("CMD > 4", cmd)
                A = cmd[0] 
            DE, C, B = cmd[l], cmd[l-2], cmd[l-3]
            print(DE, C, B, A)

        #day2
        ########
        if (len(cmd) == 1 and cmd == 1 or cmd == 2):        
            a = instruction[instruction[pos+1]]
            b = instruction[instruction[pos+2]]
            c = instruction[pos+3]
            if cmd == 1:
                instruction[c] = a + b
            if cmd == 2:
                instruction[c] = (a*b)
            ########

      pos += (len(cmd) + 1)
      # print("", intcodeprg)
    return instruction[0]

def a():
    intcodeprg = [int(n) for n in readInput().split(',')]        
    intcodeprg[1] = 12
    intcodeprg[2] = 2
    
    answ = getOutput(intcodeprg)
    print("A): ", answ)

def b():
    inp = [int(n) for n in readInput().split(',')]        
    print("B): ")

# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
