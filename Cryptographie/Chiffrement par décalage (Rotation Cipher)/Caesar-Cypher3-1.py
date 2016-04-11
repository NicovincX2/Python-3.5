# -*- coding: utf-8 -*-

# https://github.com/bt3gl/My-Gray-Hacker-Resources/blob/patch-1/Cryptography/Rotation-Ciphers/cesarCipher_simple.py

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

'''
Cesar Ecrypt
'''

import sys, os

def encrypt(message, k):
    alphabet = list('abcdefghijklmnopqrstuvwxyz ')
    cipher = ''
    for c in message:
        cipher += alphabet[(alphabet.index(c) + k)%(len(alphabet))]
    return cipher

def decrypt(message, k):
    alphabet = list('abcdefghijklmnopqrstuvwxyz ')
    decipher = ''
    for c in message:
        decipher += alphabet[(alphabet.index(c) - k)%(len(alphabet))]
    return decipher

def main():
    MESSAGE = list(raw_input('Enter the message to be encrypted: ')) or "all your basis belong to us"
    k = 13

    encrypted_msg = encrypt(MESSAGE, k)
    print("Encrypted message: " + encrypted_msg)


    decrypted_msg = decrypt(encrypted_msg, k)
    assert(decrypted_msg == MESSAGE)

if __name__ == '__main__':
    main()

 os.system("pause")