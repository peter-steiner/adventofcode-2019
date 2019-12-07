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
    #print("Amp phases: ", input)
    input_index = 0
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
          input.append(getValue(C, pos+1, instruction))
          return input
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
        
    return [1337]

def calc_thruster_power(phase_setting_sequences, instruction):
  maxAmp = 0
  amps = ["A", "B", "C", "D", "E"]
  state = []
  for ph in phase_setting_sequences:
    phase_setting = [ph[0],0]
    thruster_power = amp(phase_setting, instruction.copy())
    # First run
    for i in range(1, 5):
      thruster_power = amp([ph[i], thruster_power[-1]], instruction.copy())
      if thruster_power[-1] > maxAmp:
        maxAmp = thruster_power[-1]
        

  return maxAmp

def calc_thruster_power_feedbackloop(phase_setting_sequences, instruction):
  maxAmp = 0
  amps = ["A", "B", "C", "D", "E"]
  amplififiers = []
  for i in range(5):
    amplififiers.append(instruction.copy())

  for ph in phase_setting_sequences:
      phase_setting = [ph[0],0]
      thruster_power = amp(phase_setting, amplififiers[0])
      # First run
      for i in range(1, 5):
        thruster_power = amp([ph[i], thruster_power[-1]], amplififiers[i])
        if thruster_power[-1] > maxAmp:
          maxAmp = thruster_power[-1]
      # Feedback loop
      run = True
      while run:
        for i in range(5):
          #input = thruster_power[-1]
          thruster_power = amp([ph[i], thruster_power[-1]], amplififiers[i])
          if (amps[i] == "E" and thruster_power[-1] > maxAmp):
            maxAmp = thruster_power[-1]
            print("Setting max thruster power: ", maxAmp)
          if (len(thruster_power) == 1 and thruster_power[0] == 1337):
            print("Finished thruster power feedback loop @", amps[i])
            run = False
            break

  return maxAmp

  
def test():
    
    phase_setting_sequences = list(itertools.permutations([i for i in range(5)]))

#    instructions = ["3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"]
    instructions = ["3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0","3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0","3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"]
    for ins in instructions:
      instruction = [int(c) for c in ins.split(',')]
      thruster_power = calc_thruster_power(phase_setting_sequences, instruction)
      print(thruster_power)


def a():
  phase_setting_sequences = list(itertools.permutations([i for i in range(5)]))
  instruction = [int(n) for n in readInput().split(',')]    
  thruster_power = calc_thruster_power(phase_setting_sequences, instruction)
  
  print("A): Thruster power", thruster_power)


def b():
  phase_setting_sequences = list(itertools.permutations([i for i in range(5, 10)]))
  #print(phase_setting_sequences[0])
  instruction = [int(n) for n in readInput().split(',')]    
  thruster_power = calc_thruster_power_feedbackloop(phase_setting_sequences, instruction)
  
  print("A): Thruster power", thruster_power)

# Main body
if __name__ == '__main__':
    test()
    #a()
    b()
    sys.exit(1)
