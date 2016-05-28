# -*- coding: utf-8 -*-

# https://github.com/bt3gl/My-Gray-Hacker-Resources/blob/patch-1/Cryptography/Block_Ciphers/DES/DES_ECB_example.py

__author__ = "bt3"

from Crypto.Cipher import DES
import os


def decrypt(key, text):
    des = DES.new(key, DES.MODE_ECB)
    return des.decrypt(text)


def encrypt(key, text):
    des = DES.new(key, DES.MODE_ECB)
    return des.encrypt(text)

if __name__ == '__main__':
    text = "01234567"
    key = 'abcdefgh'
    print(encrypt(key, text))
    print(decrypt(key, text))

os.system("pause")
