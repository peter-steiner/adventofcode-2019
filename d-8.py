#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2019/day/8
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d-8"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def vefifySIF(wide, tall, image_data):
  n = wide*tall
  layers = [image_data[i * n:(i + 1) * n] for i in range((len(image_data) + n - 1) // n )]
  v_layer = []
  minZeros = sys.maxsize
  for layer in layers:
    zs = layer.count(0)
    if zs < minZeros:
      minZeros = zs
      v_layer = layer.copy()

  ones = v_layer.count(1)
  twos = v_layer.count(2)
  checksum = ones*twos
  return checksum

def printImage(wide, tall, image_data):
  n = wide*tall
  layers = [image_data[i * n:(i + 1) * n] for i in range((len(image_data) + n - 1) // n )]

  image = []
  for t in range(tall):
    image.append([-1 for w in range(wide)])

  for layer in layers:
    n = wide
    rows = [layer[i * n:(i + 1) * n] for i in range((len(layer) + n - 1) // n )]
    for row_ind in range(len(rows)):
      row = rows[row_ind]
      for bit_ind in range(len(row)):
        new = row[bit_ind]
        existing = image[row_ind][bit_ind]
        if existing == -1 or existing == 2:
          image[row_ind][bit_ind] = new

  for row in image:
    print(row)

def test():
  image_data = [int(d) for d in "123456789012"]
  h = 3
  l = 2
  chksum = vefifySIF(h,l, image_data)
  print("Checksum", chksum)

def a():
    image_data = [int(n) for n in readInput()] 
    tall = 6
    wide = 25
    chksum = vefifySIF(wide,tall, image_data)
    print("Checksum", chksum)       

def b():
    image_data = [int(n) for n in readInput()] 
    tall = 6
    wide = 25
    printImage(wide, tall, image_data)    
    
# Main body
if __name__ == '__main__':
    #test()
    a()
    b()
    sys.exit(1)
