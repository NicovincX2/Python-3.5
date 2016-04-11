# -*- coding: utf-8

# https://github.com/bt3gl/My-Gray-Hacker-Resources/blob/patch-1/Cryptography/Rotation-Ciphers/brute_force_rotation.py

import sys, os

CIPHER = "OMQEMDUEQMEK"
LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
CIPHER = ""
shift = 1

while i < len(LETTERS):
    for c in CIPHER:
        if c in LETTERS:
            CIPHER += LETTERS[(LETTERS.index(c)+shift)%(len(LETTERS))]
    print("Shift used: " + str(shift))
    print("Ciphertext: " + CIPHER)
    print("CIPHER: " + CIPHER)
    shift = shift + 1
    CIPHER = ""
 
 os.system("pause")