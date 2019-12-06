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
#task="d-6.test"
task="d-6"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    orbits = [n for n in readInput().split('\n')]    

    matching = [s for s in orbits if "COM" in s]
    print(matching)
    com = matching[0]
    orbits.remove(com)

    orbit_paths = []
    star = com.split(")")[1]
    print(star)
    orbit_paths.append([star])

    orbits.sort()
    while len(orbits) > 0:
      for orbit in orbits:
        for orbit_path in orbit_paths:
          # [S1, S2]
          S1, S2 = orbit.split(")")
          if orbit_path[-1] == S1:
            new_op = orbit_path.copy()
            new_op.append(S2)
            orbit_paths.append(new_op)
            orbits.remove(orbit)
            break

    count = 0
    for orbit_path in orbit_paths:
#      print(orbit_path)
      count += len(orbit_path)

    print("A): orbits", count)

def b():
    instructions = [n for n in readInput().split(',')]        
    answ = ""    
    print("B): ", answ)

# Main body
if __name__ == '__main__':
    # test()
    a()
    # b()
    sys.exit(1)
