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
import time

# Global variables
# task="d-5.test"
task="d-5"
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

def processInstruction(input, instruction):
    pos = 0
    while instruction[pos] != 99:
      cmd_tmp = [int(d) for d in str(instruction[pos])][::-1]
      cmd = [0,0,0,0,0]
      for i in range(len(cmd_tmp)): 
          cmd[i] = cmd_tmp[i]
      cmd = cmd[::-1]
      op = 0
      # Hantera 
      # ABCDE
      #  1002
      OP, C, B, A = 10*cmd[3] + cmd[4], cmd[2], cmd[1], cmd[0]

      if (OP == 1 or OP == 2):        
        a = getValue(C, pos+1, instruction)
        b = getValue(B, pos+2, instruction)
        c = instruction[pos+3]
        if OP == 1:
          instruction[c] = a + b
        if OP == 2:
          instruction[c] = (a*b)
        pos += 4

      # INPUT/OUTPUT
      if (OP == 3 or OP == 4):
        # print(instruction[pos:pos+2])
        if OP == 4:
          input = getValue(C, pos+1, instruction)
        if OP == 3:
          val_pos = instruction[pos+1]
          instruction[val_pos] = input
        ## do operations
        pos += 2
    return input

def processInstructionConditioner(input, instruction):
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
        print("handle op 1|2", op)
        print(instruction[pos:pos+4])
        a = getValue(C, pos+1, instruction)
        b = getValue(B, pos+2, instruction)
        c = instruction[pos+3]
        if OP == 1:
          print("a + b @ c", a, b, c)
          instruction[c] = a + b
        if OP == 2:
          print("a X b @ c", a, b, c)
          instruction[c] = (a*b)
        print("new value at", c, instruction[c])
        pos += 4

      # INPUT/OUTPUT
      if (OP == 3 or OP == 4):
        print("handle op 3|4", OP)
        print(instruction[pos:pos+2])
        if OP == 4:
          input = getValue(C, pos+1, instruction)
          print("######################################\noutput", input)
          # if input > 0:
            # break
        if OP == 3:
          val_pos = instruction[pos+1]
          instruction[val_pos] = input
        ## do operations
        pos += 2

      if (OP > 4 and OP < 9):
        first_param = getValue(C, pos+1, instruction)
        second_param  = getValue(B, pos+2, instruction)
        third_param = getValue(A, pos+3, instruction)
        if OP == 5:
          if val != 0:
            pos = second_param
          else: 
            pos += 3    
        if OP == 6:
          if val == 0:
            pos = second_param
          else: 
            pos += 3        
        if OP == 7:
          val_store = 0
          if first_param < second_param:
            val_store = 1
          instruction[third_param] = val_store
        if OP == 8:
          val_store = 0
          if first_param == second_param:
            val_store = 1
          instruction[third_param] = val_store
          
    return input

def test():
    
    # instructions = ["1002,4,3,4,33,99", "3,2,99", "3,1,4,0,99"]
    instructions = ["3,2,99"]
    input = 99
    for ins in instructions:
      print("#########", ins)
      print(ins.split(','))
      answ = processInstruction(input, [int(c) for c in ins.split(',')])
      time.sleep( 2 )

    print("A): ", answ)

def a():
    instructions = [int(n) for n in readInput().split(',')]        
    input = 1
    answ = processInstruction(input, instructions)

    print("A): ", answ)

def b():
    instructions = [int(n) for n in readInput().split(',')]        
    input = 1
    print("#########\n", instructions)
    answ = processInstructionConditioner(input, instructions)     
    
    print("B): ", answ)

# Main body
if __name__ == '__main__':
    # test()
    # a()
    b()
    sys.exit(1)
