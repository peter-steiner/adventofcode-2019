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
#task="d-3.test"
task="d-3"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

x = 1
y = 1
distance = 0
crossing = 10000
crossings = [0][0]
stepx = 0
stepy = 0
minsteps_intercerption = 1000000

def step(dir, id, panel):
  global x
  global y
  global stepx
  global stepy
  global crossing
  global minsteps_intercerption

  if dir == "U":
    y += 1
    stepy += 1
  if dir == "D":
    y -= 1 
    stepy += 1
  if dir == "R": 
    x += 1
    stepx += 1
  if dir == "L":
    x -= 1 
    stepx += 1
    
  crossings[x][y] += stepx+stepy

  if panel[x][y] != 0:
    if panel[x][y] != id:
      #print(x, y, id)
      if abs(x)+abs(y)-2 < crossing:
        crossing = abs(x)+abs(y)-2
        # print("manhattan dist:", x+y-2)
      if crossings[x][y] < minsteps_intercerption:
        minsteps_intercerption = crossings[x][y]
        # print("Distance:", minsteps_intercerption)
  panel[x][y] = id


def move(m, panel, id):
    global x
    global y 

    move = 0
    dir = "R"
    m = re.match(r"([a-z]+)(\d+)", m, re.I)
    if m:
        dir = m.group(1)
        move = int(m.group(2))
    for n in range(move):
      step(dir, id, panel)     
    


def a():
    a = 10000
    rows = [n for n in readInput().split('\n')]    
    front_panel = [[0 for x in range(a)] for y in range(a)]  
    global x
    global y 
    global stepx
    global stepy
    global crossing
    global crossings

    crossings = [[0 for x in range(a)] for y in range(a)]  
    front_panel[x][y] = 1

    id = int(0)
    for row in rows:
        x = 1
        y = 1
        stepx = 0
        stepy = 0
        id += 1
        for m in [n for n in row.split(',')]:
  #          print(m)
            move(m, front_panel, id)
 #       print("cabel drawn")

    print("A): ", crossing)

def b():
    a = 10000
    rows = [n for n in readInput().split('\n')]    
    front_panel = [[0 for x in range(a)] for y in range(a)]  
    global x
    global y 
    global crossing
    global crossings
    global minsteps_intercerption

    crossings = [[0 for x in range(a)] for y in range(a)]  
    front_panel[x][y] = 1

    id = 0
    for row in rows:
        x = 1
        y = 1
        stepx = 0
        stepy = 0
        id += 1
        for m in [n for n in row.split(',')]:
            move(m, front_panel, id)

    print("Distance:", minsteps_intercerption)


# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
