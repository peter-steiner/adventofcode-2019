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

def getOutput(intcodeprg):
    pos = 0
    while intcodeprg[pos] != 99:
      #print("po: ", intcodeprg[pos])
      cmd = intcodeprg[pos]
      a = intcodeprg[intcodeprg[pos+1]]
      b = intcodeprg[intcodeprg[pos+2]]
      c = intcodeprg[pos+3]
      # print("", a, b, c, len(intcodeprg))
      if cmd == 1:
          intcodeprg[c] = a + b
      if cmd == 2:
          intcodeprg[c] = (a*b)
      pos += 4
      # print("", intcodeprg)
    return intcodeprg[0]

def a():
    intcodeprg = [int(n) for n in readInput().split(',')]        
    intcodeprg[1] = 12
    intcodeprg[2] = 2
    
    answ = getOutput(intcodeprg)
    print("A): ", answ)

def b():
    intcodeprg = [int(n) for n in readInput().split(',')]        
    intcodeprg[1] = 12
    intcodeprg[2] = 2

    for n in range(100):
      for k in range(100):
        intcodeprg[1] = n
        intcodeprg[2] = k
        try:
          # print(n, k)
          answ = getOutput(intcodeprg.copy())
          # print("", answ)
          if answ ==  19690720:
            print("noun/verb", n, k, 100*n+k)          
        except:
          pass
    # print("B): ", totsum)

# Main body
if __name__ == '__main__':
    # a()
    b()
    sys.exit(1)
