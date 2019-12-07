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
#task="d-7.test"
task="d-7"
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
      print('AmpState: ', self.id, self.pos, self.phase, self.instruction, self.input, self.output, self.done, self.visits)

def getValue(mode, pos, instruction):
  val = instruction[pos]
  if mode == 0:
    return instruction[val]
  return val

def amp(amplifier_state):

    if amplifier_state.visits == 0:
      input = [amplifier_state.phase, amplifier_state.input]
    else: 
      input = [amplifier_state.input]
    amplifier_state.visits += 1
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
          amplifier_state.pos = pos +2
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
    
    phase_setting_sequences = list(itertools.permutations([i for i in range(5, 10)]))
    #instructions = ["3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"]
    instructions = ["3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"]

    for ins in instructions:
      instruction = [int(c) for c in ins.split(',')]
      thruster_power = calc_thruster_power_feedbackloop(phase_setting_sequences, instruction)
      print(thruster_power)

def b():
  phase_setting_sequences = list(itertools.permutations([i for i in range(5, 10)]))
  instruction = [int(n) for n in readInput().split(',')]    
  thruster_power = calc_thruster_power_feedbackloop(phase_setting_sequences, instruction)
  
  print("B): Thruster power", thruster_power)

# Main body
if __name__ == '__main__':
    #test()
    b()
    sys.exit(1)
