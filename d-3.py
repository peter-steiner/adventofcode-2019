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

class Wire:
  def __init__(self,  id = 0, x = 1, y = 1, sx = 0, sy = 0):
    self.id = id
    self.x = x
    self.y = y
    self.stepx = sx
    self.stepy = sy
  
  def move(self, direction):
    if direction == "U":
      self.y += 1
      self.stepy += 1
    if direction == "D":
      self.y -= 1 
      self.stepy += 1
    if direction == "R": 
      self.x += 1
      self.stepx += 1
    if direction == "L":
      self.x -= 1 
      self.stepx += 1 

  def print(self):
    print('Wire', self.x, self.y, self.stepx, self.stepy)

class FrontPanel:
  def __init__(self, a = 10000):
    self.a = a
    self.front_panel = [[0 for x in range(a)] for y in range(a)]  
    self.front_panel[1][1] = 0
    self.steps_per_cordinate = [[0 for x in range(a)] for y in range(a)]  

    self.manhattan_distance = 1000 
    self.minsteps_interc = 1000000

  def print(self):
    print('Front panel', self.manhattan_distance, self.minsteps_interc)

def isWireCrossing(wire, panel):
  x, y = wire.x, wire.y
  #Is there a wire at possition
  if panel.front_panel[x][y] != 0:
    #Its another wire  
    return panel.front_panel[x][y] != wire.id
  return False

def step(wire, direction, panel):
  wire.move(direction)
  #wire.print()
  x, y = wire.x, wire.y
  # sum all steps for all cords hence +=
  panel.steps_per_cordinate[x][y] += wire.stepx+wire.stepy
 
  if isWireCrossing(wire, panel):
    if abs(x)+abs(y)-2 < panel.manhattan_distance:
      panel.manhattan_distance = abs(x)+abs(y)-2
    if panel.steps_per_cordinate[x][y] < panel.minsteps_interc:
      panel.minsteps_interc = panel.steps_per_cordinate[x][y]
  
  # Mark visited      
  panel.front_panel[x][y] = wire.id


def move(wire, move, panel):
    steps, dir = 0, "R"
    m = re.match(r"([a-z]+)(\d+)", move, re.I)
    if m:
      dir = m.group(1)
      steps = int(m.group(2))
    for n in range(steps):
      step(wire, dir, panel)     


def a_b():
    rows = [n for n in readInput().split('\n')]    
    panel = FrontPanel()
  
    wire_id = 0
    for row in rows:
        wire_id += 1
        wire = Wire(wire_id)  
        print("Pull new wire", wire_id)    
        for m in [n for n in row.split(',')]:
          move(wire, m, panel)
    
    #panel.print()
    print("A): Manhattan distance: ", panel.manhattan_distance)
    print("B): Least steps to interception:", panel.minsteps_interc)


# Main body
if __name__ == '__main__':
    a_b()
    sys.exit(1)
