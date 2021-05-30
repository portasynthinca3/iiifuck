#!/usr/bin/env python3

import sys, os

iii_map = {
    'II': '>',
    'Il': '<',
    'I|': '+',
    'lI': '-',
    'll': '.',
    'l|': ',',
    '|I': '[',
    '|l': ']'
}
iii_rev_map = {v: k for k, v in iii_map.items()}

def detranspile(program):
    output = ''
    if len(program) % 2 != 0: raise SyntaxError("Invalid syntax")
    for pc in range(0, len(program), 2):
        instr = program[pc:pc+2]
        if instr not in iii_map: raise SyntaxError(f"Invalid syntax at {pc}")
        output += iii_map[instr]
    return output

def transpile(program):
    output = ''
    for pc in range(0, len(program)):
        instr = program[pc]
        if instr not in iii_rev_map: continue
        output += iii_rev_map[instr]
    return output

args = sys.argv
if len(args) != 3: print('Usage: ./iiitransp.py (de)transpile input.{bf,ifff}')

inp = open(args[2], 'r').read()
out = open(os.path.splitext(args[2])[0] + '.iiif', 'w')

out.write(transpile(inp) if args[1] == 'transpile' else detranspile(inp))
out.close()