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
  print("mode", mode)
  val = instruction[pos]
  if mode == 0:
    return instruction[val]
  if mode == 1:
    return val
  if mode == 2:
    print("mode 2", mode, amplifier_state.rel_base, val, instruction[amplifier_state.rel_base])
    amplifier_state.rel_base += val
    amplifier_state.pos = amplifier_state.rel_base
    pos = amplifier_state.rel_base
    return instruction[amplifier_state.rel_base]

def amp(amplifier_state):

    # if amplifier_state.visits == 0:
    #   input = [amplifier_state.phase, amplifier_state.input]
    # else:
    input = [amplifier_state.input]
    amplifier_state.visits += 1
    instruction = [0 for i in range(10000)]
    for i in range(len(amplifier_state.instruction)):
      instruction[i] = amplifier_state.instruction[i]
    pos = amplifier_state.pos

    input_index = 0
    while instruction[pos] != 99:
      time.sleep(2)
      print("run", pos)
      amplifier_state.print()
      cmd_tmp = [int(d) for d in str(instruction[pos])][::-1]
      cmd = [0,0,0,0,0]
      for i in range(len(cmd_tmp)):
          cmd[i] = cmd_tmp[i]
      cmd = cmd[::-1]
      OP, C, B, A = 10*cmd[3] + cmd[4], cmd[2], cmd[1], cmd[0]
      print("CMD", cmd)
      if (OP == 1 or OP == 2):
        a = getValue(C, amplifier_state, pos+1, instruction)
        b = getValue(B, amplifier_state, pos+2, instruction)
        c = instruction[pos+3]
        print("c", c)
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
          amplifier_state.pos = pos +2
          print("output: ", output)
          #return amplifier_state
        if OP == 3:
          print("handle input")
          val_pos = instruction[pos+1]
          instruction[val_pos] = input[input_index]
          input_index += 1
        pos += 2
      if OP == 9:
        val_pos = instruction[pos+1]
        value = getValue(C, amplifier_state, pos+1, instruction)
        amplifier_state.rel_base = value
        print("Set new rel base", pos, value, amplifier_state.rel_base)
        pos += 2

      if (OP > 4 and OP < 9):
        first_param = getValue(C, amplifier_state, pos+1, instruction)
        second_param  = getValue(B, amplifier_state, pos+2, instruction)
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

    amplifier_state.done = True
    return amplifier_state

def printStates(amplififiers):
  for i in range(5):
    amplififiers[i].print()
  print("#####################")

def calc_thruster_power_feedbackloop(phase_setting_sequences, instruction):
  maxAmp = 0
  amps = ["A", "B", "C", "D", "E"]
  #phase_setting_sequences = [[9,8,7,6,5]]

  for ph in phase_setting_sequences:

      amplifiers = []
      for i in range(5):
        amp_state = AmpState(amps[i], 0, 0, instruction.copy(), 0,  0)
        amplifiers.append(amp_state)

      amplifiers[0].phase = ph[0]
      prev_amp_state = amp(amplifiers[0])
      # First run
      for i in range(1, 5):
        amplifier = amplifiers[i]
        amplifier.input = prev_amp_state.output
        amplifier.phase = ph[i]
        prev_amp_state = amp(amplifier)
        if (prev_amp_state.id == "E" and prev_amp_state.output > maxAmp):
          maxAmp = prev_amp_state.output

      #Feedback loop
      run = True
      while run:
        for i in range(5):
          amplifier = amplifiers[i]
          amplifier.input = prev_amp_state.output
          prev_amp_state = amp(amplifier)
          if (prev_amp_state.id == "E" and prev_amp_state.output > maxAmp):
            maxAmp = prev_amp_state.output
            #print("Setting max thruster power: ", maxAmp)
          if (prev_amp_state.id == "E" and prev_amp_state.done):
            #print("Finished thruster power feedback loop @", prev_amp_state.id, prev_amp_state.output)
            #prev_amp_state.print()
            run = False
            break

  return maxAmp



def test():

    #phase_setting_sequences = list(itertools.permutations([i for i in range(5, 10)]))
    #instructions = ["1102,34915192,34915192,7,4,7,99,0"]
    #instructions = ["104,1125899906842624,99"]
    instructions = ["109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"]

    for ins in instructions:
      instruction = [int(c) for c in ins.split(',')]
      input = 1
      amp_state = AmpState("A", 0, 1, instruction.copy(), input,  0)
      amp(amp_state)
      amp_state.print()

def a():
  instruction = [int(n) for n in readInput().split(',')]
  print(instruction)
  input = 1
  amp_state = AmpState("A", 0, 1, instruction.copy(), input,  0)
  amp(amp_state)
  amp_state.print()

  print("B): Thruster power", amp_state.output)

# Main body
if __name__ == '__main__':
    test()
    #a()
    sys.exit(1)
