# -*- coding: utf-8 -*-

import os

'''
..    . .. .  . .. ...  ... .   . ..... ..    . ..  ..  ...  . 
....... ....... ....... ....... ....... ....... ....... .......
..    . .. .  . ..  .   . ..... .. .... ..  ..  . ..... .. ... 
....... ....... ....... ....... ....... ....... ....... .......
.. .... . ..... ..  ... .. .    .. .... ...  .. ... .   ...  ..
....... ....... ....... ....... ....... ....... ....... .......
'''

s = """1100001 1101001 1101110 1110100 1011111 1100001 1100110 1110010 1100001 1101001 1100100 1011111 1101111 1100110 1011111 1101110 1101111 1011111 1100111 1101000 1101111 1110011 1110100 1110011"""

a = ''.join(chr(int(i, 2)) for i in s.replace("\n", " ").split(' '))

print(a)

os.system("pause")
