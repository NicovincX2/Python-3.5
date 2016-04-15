# -*- coding: utf-8 -*-

# https://github.com/bt3gl/My-Gray-Hacker-Resources/blob/patch-1/Cryptography/Block_Ciphers/AES/aes_simple_example.py

def example_aes():
    from Crypto.Cipher import AES
    IV = '1234567890123456'
    KEY = 'Hello There!'
    obj = AES.new(KEY, AES.MODE_CBC, IV)
    message = "The answer is no"
    ciphertext = obj.encrypt(message)
    print ciphertext
    obj2 = AES.new(KEY, AES.MODE_CBC, IV)
    print obj2.decrypt(ciphertext)

if __name__ == '__main__':
    example_aes()

 os.system("pause")