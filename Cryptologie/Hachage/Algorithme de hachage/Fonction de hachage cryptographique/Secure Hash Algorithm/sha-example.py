# -*- coding: utf-8 -*-

import os

def example_sha():
    from Crypto.Hash import SHA256
    hash = SHA256.new()
    hash.update('message'.encode('utf-8'))
    print (hash.digest())

if __name__ == '__main__':
    example_sha()

os.system("pause")
