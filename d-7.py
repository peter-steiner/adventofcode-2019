#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2019/day/7
"""

# Imports
import sys
import os
import re
import math
import time
import itertools

# Global variables
task="d-7.test"
#task="d-7"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def getValue(mode, pos, instruction):
  val = instruction[pos]
  if mode == 0:
    return instruction[val]
  return val

def amp(input, instruction):
    pos = 0
    while instruction[pos] != 99:
      cmd_tmp = [int(d) for d in str(instruction[pos])][::-1]
      cmd = [0,0,0,0,0]
      for i in range(len(cmd_tmp)): 
          cmd[i] = cmd_tmp[i]
      cmd = cmd[::-1]
      op = 0
      OP, C, B, A = 10*cmd[3] + cmd[4], cmd[2], cmd[1], cmd[0]
      if (OP == 1 or OP == 2):        
        # print("handle OP 1|2", OP)
        # print(instruction[pos:pos+4])
        a = getValue(C, pos+1, instruction)
        b = getValue(B, pos+2, instruction)
        c = instruction[pos+3]
        if OP == 1:
          # print("a + b @ c", a, b, c)
          instruction[c] = a + b
        if OP == 2:
          # print("a X b @ c", a, b, c)
          instruction[c] = (a*b)
        # print("new value at", c, instruction[c])
        pos += 4

      # INPUT/OUTPUT
      if (OP == 3 or OP == 4):
        if OP == 4:
          input = getValue(C, pos+1, instruction)
        if OP == 3:
          val_pos = instruction[pos+1]
          instruction[val_pos] = input
        pos += 2
      
      if (OP > 4 and OP < 9):
        first_param = getValue(C, pos+1, instruction)
        second_param  = getValue(B, pos+2, instruction)
        if OP == 5:
          if first_param != 0:
            pos = second_param
          else: 
            pos += 3    
        if OP == 6:
          if first_param == 0:
            pos = second_param
          else: 
            pos += 3 
        if OP == 7:
          third_param = instruction[pos+3]
          val_store = 0
          if first_param < second_param:
            val_store = 1
          instruction[third_param] = val_store
          pos +=4
        if OP == 8:
          third_param = instruction[pos+3]
          val_store = 0
          if first_param == second_param:
            val_store = 1
          instruction[third_param] = val_store
          pos +=4
        
    return input

def calc_thruster_power(phase_setting_sequences, instruction):
  print("#########\n", instruction)

  phase_setting = [1,0]
  thruster_power = amp(phase_setting, instruction)
  time.sleep( 2 )

  return thruster_power
  
def test():
    
    phase_setting_sequences = list(itertools.permutations([i for i in range(5)]))

    # instructions = ["1002,4,3,4,33,99", "3,2,99", "3,1,4,0,99"]
    instructions = ["3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0","3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0","3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"]
    for ins in instructions:
      instruction = [int(c) for c in ins.split(',')]
      thruster_power = calc_thruster_power(phase_setting_sequences, instruction)
      print(thruster_power)


def a():
    orbits = [n for n in readInput().split('\n')]    
    print("A): orbits", count)


# Main body
if __name__ == '__main__':
    test()
    #a()
    sys.exit(1)
