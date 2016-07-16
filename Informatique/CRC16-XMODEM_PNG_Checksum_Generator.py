# -*- coding: utf-8 -*-

# Creates a PNG with a checksum chosen via XRX16-XMODEM

import os
from itertools import product
import crcmod.predefined
from math import factorial
import string
import crc16

# Init variables
found = False
currLen = 1
txtTarget = ""
crcTarget = 0

# Init functions
def crc(data):
        return crc16.crc16xmodem(data.encode(encoding='utf_8'))

def nCr(n,r):
    f = factorial
    return round(f(n) / f(r) / f(n-r))

# crcTarget = 11181                       # CRC16-XMODEM of '87d41d15f' as Hex - 0x2bad
crcTarget = 42606
print ("CRC of target: " + hex(crcTarget))

png_header = "\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52"

# crcTarget = "\x87\xd4\x1d\x15\x0f"      # Entire thing
# print ("CRC of target: " + crcTarget)

availableChars = string.printable

# Main loop
while True:

        # Get new combinations
        print ("\nGenerating CRC's of all combinations of " + str(currLen) + " characters...")
        print ("         (Total of " + str(nCr(len(availableChars),currLen)) + " combinations)")

        for possibleCombination in product(availableChars, repeat=currLen):
            currTxt = "".join(possibleCombination)
            currCrc = crc(png_header+currTxt)
            if currCrc == crcTarget:
                found = True
                if currTxt == txtTarget:
                    print ("         ORIGINAL FOUND (" + currTxt + ": " + hex(currCrc) + ")")
                else:
                    print ("         COLLISION FOUND: " + currTxt + ": " + hex(currCrc))

        currLen = currLen + 1

        if found:
            pass
            # break
        else:
            print ("         Nothing found.")

os.system("pause")
