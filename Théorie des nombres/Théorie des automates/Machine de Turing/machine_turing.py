# -*- coding: utf-8 -*-

import os

# Turing Machine simulator to add unary numbers (e.g. 11 + 111)
#
# prog is indexed by the current tape symbol (0 or 1) and then by state
# (a kind of instruction pointer) to get an 'instruction' comprising:
#   symbol to write on current tape position,
#   head action (-1 = move left, +1 = move right)
#   next state (like a goto jump).

#       symbol 0    symbol 1
prog = [[(1, +1, 1), (1, +1, 0)],           # state 0
        [(0, -1, 2), (1, +1, 1)],           # state 1
        [(0, +1, 2), (0, +1, 9)]]           # state 2
tape = [1, 1, 0, 1, 1, 1, 0, 0, 0]                  # The data tape
head = 0                                    # head position on tape
state = 0                                   # instruction pointer
print(tape)
while state != 9:                           # while not halt:
    symbol = tape[head]                         # read current tape symbol
    symbol, dir, state = t = prog[state][symbol]  # lookup instruction
    print(' ' * (head * 3 + 1) + '^  ' + str(t))  # display progress
    tape[head] = symbol                         # write new symbol on tape
    print(tape)
    head = head + dir                           # move tape head

os.system("pause")
