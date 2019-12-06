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
      count += len(orbit_path)

    YOU = []
    SAN = []
    for path in orbit_paths:
      YOU_ = [s for s in path if "YOU" in s]
      SAN_ = [s for s in path if "SAN" in s]
      if len(YOU_) > 0:
        YOU = path
      if len(SAN_) > 0:
        SAN = path 

    #print("You", YOU)
    #print("San", SAN)

    diff1 = list(set(YOU) - set(SAN))
    diff2 = list(set(SAN) - set(YOU))
    print(diff1, len(diff1))
    print(diff2, len(diff2))

    orbital_transfers = len(diff1)-1 + len(diff2)-1
    print("A): orbits", count)
    print("B): orbital_transfers", orbital_transfers)


# Main body
if __name__ == '__main__':
    # test()
    a()
    sys.exit(1)
