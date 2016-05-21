# -*- coding: utf-8 -*-

# https://github.com/bt3gl/My-Gray-Hacker-Resources/blob/patch-1/Cryptography/Stream_Ciphers/arc4.py

import os
from Crypto.Cipher import ARC4

obj1 = ARC4.new('01234567')
obj2 = ARC4.new('01234567')

text = 'abcdefghijklmnop'
cipher_text = obj1.encrypt(text)
print (cipher_text)
print (obj2.decrypt(cipher_text))

os.system("pause")
