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
task="d-3.test"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

x = 1
y = 1
distance = 0

def move(m, panel, id):
    global x
    global y 

    move = 0
    dir = "R"
    m = re.match(r"([a-z]+)(\d+)", m, re.I)
    if m:
        dir = m.group(1)
        move = int(m.group(2))

    print("m", dir, move)
    
    if dir == "U":
        for n in range(move):
            panel[x][y+1] = id 
            y += 1
    if dir == "R": 
        for n in range(move):
            panel[x+1][y] = id 
            x += 1

    if dir == "L":
        for n in range(move):
            panel[x-1][y] = id
            x -= 1 
    if dir == "D":
        for n in range(move):
            panel[x][y-1] = id
            y -= 1 

    if panel[x][y] > 0:
        print(panel[x][y], id)
        if panel[x][y] != id:
            print("#######crossing", x, y)
            print("###################Dist:", x+y-2)

    #for n in range(10):
       #print(panel[9-n])
    


def a():
    rows = [n for n in readInput().split('\n')]    
    front_panel = [[0 for x in range(10)] for y in range(10)]  
    global x
    global y 

    front_panel[x][y] = 1

    id = 0
    for row in rows:
        x = 1
        y = 1
        id += 1
        for m in [n for n in row.split(',')]:
            print(m)
            move(m, front_panel, id)
        print("cabel drawn")

    print("A): ", rows)

def b():
    inp = [n for n in readInput().split(',')]        
    print("B): ", inp)


# Main body
if __name__ == '__main__':
    a()
    #b()
    sys.exit(1)
