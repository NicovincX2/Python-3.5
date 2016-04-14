# -*- coding: utf-8 -*-

import os

def is_numeric(lit):
    'Return value of numeric literal string or ValueError exception'
 
    # Handle '0'
    if lit == '0': return 0
    # Hex/Binary
    litneg = lit[1:] if lit[0] == '-' else lit
    if litneg[0] == '0':
        if litneg[1] in 'xX':
            return int(lit,16)
        elif litneg[1] in 'bB':
            return int(lit,2)
        else:
            try:
                return int(lit,8)
            except ValueError:
                pass
 
    # Int/Float/Complex
    try:
        return int(lit)
    except ValueError:
        pass
    try:
        return float(lit)
    except ValueError:
        pass
    return complex(lit)

for s in ['0', '00', '123', '-123.', '-123e-4', '0123', '0x1a1', '-123+4.5j', '0b0101', '0.123', '-0xabc', '-0b101']:
    print "%14s -> %-14s %s" % ('"'+s+'"', is_numeric(s), type(is_numeric(s)))

os.system("pause")