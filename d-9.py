#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2019/day/9
"""

# Imports
import sys
import os
import re
import math
import time
import itertools

# Global variables
#task="d-9.test"
task="d-9"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

class AmpState:
  def __init__(self,  id = "X", pos = 0, phase = 0, instruction = [], input = 0, output = 0):
    self.id = id
    self.pos = pos
    self.phase = phase
    self.instruction = instruction
    self.input = input
    self.output = output
    self.done = False
    self.visits = 0
    self.rel_base = 0

  def printInstruction(self):
    print('AmpState instruction: ', self.instruction)

  def print(self):
    print('AmpState: ', self.id, self.pos, self.rel_base, self.phase, self.instruction, self.input, self.output, self.done, self.visits)

def getValue(mode, amplifier_state, pos, instruction):
  # print("Get val mode", mode, amplifier_state.rel_base, pos, instruction[pos])
  val = instruction[pos]
  if mode == 0:
    # print("Positional")
    return instruction[val]
  if mode == 1:
    # print("Absolute")
    return val
  if mode == 2:
    #print("Rel val {} {}".format(instruction[amplifier_state.rel_base + val], amplifier_state.rel_base + val))
    return instruction[amplifier_state.rel_base + val]

def getPos(mode, amplifier_state, pos, instruction):
  if mode == 2:
    #print("REALTIVE POS {} {}".format(amplifier_state.rel_base, amplifier_state.rel_base + instruction[pos]))
    return amplifier_state.rel_base + instruction[pos]
  return instruction[pos]

def amp(amplifier_state):

    input = amplifier_state.input
    amplifier_state.visits += 1
    instruction = [0 for i in range(10000)]
    for i in range(len(amplifier_state.instruction)):
      instruction[i] = amplifier_state.instruction[i]
    pos = amplifier_state.pos

    while instruction[pos] != 99:
      cmd_tmp = [int(d) for d in str(instruction[pos])][::-1]
      cmd = [0,0,0,0,0]
      for i in range(len(cmd_tmp)):
          cmd[i] = cmd_tmp[i]
      cmd = cmd[::-1]
      OP, C, B, A = 10*cmd[3] + cmd[4], cmd[2], cmd[1], cmd[0]
      #print("CMD", cmd, pos)
      if (OP == 1 or OP == 2):
        a = getValue(C, amplifier_state, pos+1, instruction)
        b = getValue(B, amplifier_state, pos+2, instruction)
        c = getPos(A, amplifier_state, pos+3, instruction)
        if OP == 1:
          instruction[c] = a + b
        if OP == 2:
          instruction[c] = (a*b)
        pos += 4

      # INPUT/OUTPUT
      if (OP == 3 or OP == 4):
        if OP == 4:
          output = getValue(C, amplifier_state, pos+1, instruction)
          amplifier_state.output = output
          input = output
          print("##########\nOutput: ", output)
          print("##########")
        if OP == 3:
#          print("OP 3 pos:{} inp:{}".format(pos, input))
          instruction[amplifier_state.rel_base + instruction[pos+1]] = input
        pos += 2
      if OP == 9:
        value = getValue(C, amplifier_state, pos+1, instruction)
        rb = amplifier_state.rel_base
 #       print("OP 9 RB old: {} new: {} pos: {} val: {}".format(rb, rb + value, pos+1, value))
        amplifier_state.rel_base += value
        pos += 2

      if (OP > 4 and OP < 9):
        first_param = getValue(C, amplifier_state, pos+1, instruction)
        second_param  = getValue(B, amplifier_state, pos+2, instruction)
        third_param = getPos(A, amplifier_state, pos+3, instruction)
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
          val_store = 0
          if first_param < second_param:
            val_store = 1
          instruction[third_param] = val_store
          pos +=4
        if OP == 8:
          val_store = 0
          if first_param == second_param:
            val_store = 1
          instruction[third_param] = val_store
          pos +=4

    amplifier_state.done = True
    return amplifier_state


def test():
    #instructions = ["1102,34915192,34915192,7,4,7,99,0"]
    #instructions = ["104,1125899906842624,99"]
    instructions = ["109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"]
    print("wdawd")
    for ins in instructions:
      instruction = [int(c) for c in ins.split(',')]
      input = 0
      amp_state = AmpState("A", 0, 1, instruction.copy(), input,  0)
      amp(amp_state)
      amp_state.print()

def a():
  instruction = [int(n) for n in readInput().split(',')]
  input = 1
  amp_state = AmpState("A", 0, 1, instruction.copy(), input,  0)
  amp(amp_state)

  print("a): Thruster power", amp_state.output)

def b():
  instruction = [int(n) for n in readInput().split(',')]
  input = 2
  amp_state = AmpState("A", 0, 1, instruction.copy(), input,  0)
  amp(amp_state)

  print("a): Thruster power", amp_state.output)

# Main body
if __name__ == '__main__':
    # test()
    a()
    #b()
    sys.exit(1)
