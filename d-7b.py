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

class AmpState:
  def __init__(self,  id = "X", pos = 0, phase = 0, instruction = [], input = 0, output = 0):
    self.id = id
    self.pos = pos
    self.instruction = instruction
    self.phase = phase
    self.input = input
    self.output = output
    self.done = False
    self.visits = 0

  def print(self):
      print('AmpState: ', self.id, self.pos, self.instruction, self.phase, self.input, self.output, self.done, self.visits)

def getValue(mode, pos, instruction):
  val = instruction[pos]
  if mode == 0:
    return instruction[val]
  return val

def amp(amplifier_state):

    amplifier_state.visits += 1
    #amplifier_state.print()
    input = [amplifier_state.phase, amplifier_state.input]
    instruction = amplifier_state.instruction
    pos = amplifier_state.pos

    input_index = 0
    while instruction[pos] != 99:
      cmd_tmp = [int(d) for d in str(instruction[pos])][::-1]
      cmd = [0,0,0,0,0]
      for i in range(len(cmd_tmp)): 
          cmd[i] = cmd_tmp[i]
      cmd = cmd[::-1]
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
        if OP == 4:
          output = getValue(C, pos+1, instruction)
          amplifier_state.output = output
          amplifier_state.pos = pos + 2
          amplifier_state.print()
          return amplifier_state
        if OP == 3:
          val_pos = instruction[pos+1]
          instruction[val_pos] = input[input_index]
          input_index += 1
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
    
    amplifier_state.done = True
    return amplifier_state

def printStates(amplififiers):
  for i in range(5):
    print(amplififiers[i].print())

def calc_thruster_power_feedbackloop(phase_setting_sequences, instruction):
  maxAmp = 0
  amps = ["A", "B", "C", "D", "E"]
  
  for ph in phase_setting_sequences:

      amplififiers = []
      for i in range(5):
        #id = 0, pos = 0, phase = 0, instruction = [], input = 0, output = 0
        amp_state = AmpState(amps[i], 0, 0, instruction.copy(), 0,  0)
        amplififiers.append(amp_state)

      amplififiers[0].phase = ph[0]
      prev_amp_state = amp(amplififiers[0])
      # First run
      for i in range(1, 5):
        amplifier = amplififiers[i]
        amplifier.input = prev_amp_state.output
        prev_amp_state = amp(amplifier)
        if (prev_amp_state.id == "E" and prev_amp_state.output > maxAmp):
          maxAmp = prev_amp_state.output

      printStates(amplififiers)
      # Feedback loop
      # run = True
      # while run:
      #   for i in range(5):
      #     amplifier = amplififiers[i]
      #     amplifier.input = prev_amp_state.output
      #     prev_amp_state = amp(amplifier)
      #     if (prev_amp_state.id == "E" and prev_amp_state.output > maxAmp):
      #       maxAmp = prev_amp_state.output
      #       print("Setting max thruster power: ", maxAmp)
      #     if (prev_amp_state.id == "E" and prev_amp_state.done):
      #       print("Finished thruster power feedback loop @", prev_amp_state.id, prev_amp_state.output)
      #       #prev_amp_state.print()
      #       run = False
      #       break

  return maxAmp


  
def test():
    
    phase_setting_sequences = list(itertools.permutations([i for i in range(5)]))

    instructions = ["3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"]
#    instructions = ["3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5",
#    "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"]

    for ins in instructions:
      instruction = [int(c) for c in ins.split(',')]
      thruster_power = calc_thruster_power_feedbackloop(phase_setting_sequences, instruction)
      print(thruster_power)

def b():
  phase_setting_sequences = list(itertools.permutations([i for i in range(5, 10)]))
  #print(phase_setting_sequences[0])
  instruction = [int(n) for n in readInput().split(',')]    
  thruster_power = calc_thruster_power_feedbackloop(phase_setting_sequences, instruction)
  
  print("A): Thruster power", thruster_power)

# Main body
if __name__ == '__main__':
    test()
    #b()
    sys.exit(1)
