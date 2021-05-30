#!/usr/bin/env python3

import sys, readchar

def find_bracket(program, start, what, inc):
    ctr = 0
    initial = program[start:start+2]
    for pc in range(start, -2 if inc < 0 else len(program), inc):
        if program[pc:pc+2] == initial:
            ctr += 1
        elif program[pc:pc+2] == what:
            ctr -= 1
        if ctr == 0:
            return pc

def iiifuck(program):
    tape = [0] * 30000
    head = 0
    pc = 0

    while pc < len(program):
        instr = program[pc:pc+2]
        if instr == 'II':
            head += 1
        elif instr == 'Il':
            head -= 1
        elif instr == 'I|':
            tape[head] += 1
            if tape[head] > 255: tape[head] = 0
        elif instr == 'lI':
            tape[head] -= 1
            if tape[head] < 0: tape[head] = 255
        elif instr == 'll':
            print(chr(tape[head]), end='')
        elif instr == 'l|':
            tape[head] = ord(readchar.readchar())
        elif instr == '|I':
            if tape[head] == 0:
                pc = find_bracket(program, pc, '|l', 2)
        elif instr == '|l':
            if tape[head] != 0:
                pc = find_bracket(program, pc, '|I', -2)
        pc += 2

args = sys.argv
if len(args) != 2: print('Usage: ./iiifuck.py input.iiif')

iiifuck(open(args[1], 'r').read())