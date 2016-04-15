# -*- coding: utf-8 -*-

import os
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

key = RSA.generate(1024)
text = 'abcdefgh'

hash = SHA256.new(text).digest()
print hash

signature = key.sign(hash, '')
print signature

os.system("pause")