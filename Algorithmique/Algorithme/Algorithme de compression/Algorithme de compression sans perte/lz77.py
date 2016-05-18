# -*- coding: utf-8 -*-

# http://nbviewer.jupyter.org/github/yoavram/CS1001.py/blob/master/recitation12.ipynb

import os
from time import perf_counter

def find_max_repetition(text, index, window_length=2**12-1, max_rep_length=2**5-1):
    """ finds a maximum repetition in the text.
    Returns offset and length of the longest repetition.
    Returned offset is smallest one (closest to index) among all max matches"""
    assert isinstance(text, str)
    repitition_length = 0 # length of max repitition
    repitition_offset = 0 # distance backwards to begining of max repitition
    for offset in range(1, min(index + 1, window_length)):
        current_length = 0
        while current_length < min(max_rep_length, len(text) - index) and text[index - offset + current_length] == text[index + current_length]:
            current_length += + 1
        if repitition_length < current_length:
            repitition_length = current_length
            repitition_offset = offset
    return repitition_offset, repitition_length

def test_find_max_repetition(text, index):
    offset, length = find_max_repetition(text, index)
    print(text[index:index + length])
    print(text[index-offset:index - offset + length])
    return text[index:index + length] == text[index - offset:index - offset + length]

find_max_repetition("abracadabra", 7)
find_max_repetition("xyzxyzwxyzw", 3)
find_max_repetition("xyzxyzwxyzw", 7)
find_max_repetition('aaaaa', 1)

def lz77_compress(text, window_length=2**12-1, max_rep_length=2**5-1):
    """LZ77 compression of ASCII text.
    Produces a list comprising of either ascii character
    or by a pair [m,k] where m is an offset and
    k is a match (both are non negative integers)"""
    result = []
    index = 0
    while index < len(text):
        if ord(text[index]) >= 128:
            # non-ascii
            index += 1
            continue
        offset, length = find_max_repetition(text, index, window_length, max_rep_length)
        if length < 3:
            # no repetition or a single character repetition
            result.append(text[index])
            index += 1
        else:
            result.append((offset, length))   # two or more chars in repetition
            index += length
    return result  # produces a list composed of chars and pairs

print(lz77_compress("You know what I hate, you know what I hate, you know what I hate? Repetitions!"))

welcome = '''Welcome my son, welcome to the machine.
Where have you been? It's alright we know where you've been.
You've been in the pipeline, filling in time,
Provided with toys and Scouting for Boys.
You bought a guitar to punish your ma,
And you didn't like school, and you know you're nobody's fool,
So welcome to the machine.
Welcome my son, welcome to the machine.
What did you dream? It's alright we told you what to dream.
You dreamed of a big star, he played a mean guitar,
He always ate in the Steak Bar. He loved to drive in his Jaguar.
So welcome to the machine.'''

welcome_intermediate = lz77_compress(welcome)
print(welcome_intermediate)

def char2bits(ch):
    ''' convert a character to int and then format it to binary
    using exactly 7 bits '''
    return '{:07b}'.format(ord(ch))
print(char2bits('1'))
print(char2bits('z'))

print(bin(ord('1'))[2:])
print(char2bits('1'))

import math
def intermediate2bits(compressed, window_length=2**12-1, max_rep_length=2**5-1):
   """ converts intermediate format compressed list
       to a string of bits"""
   offset_width = math.ceil(math.log(window_length, 2))
   length_width = math.ceil(math.log(max_rep_length,2))

   result = []
   for item in compressed:
      if isinstance(item, str):
         result.append("0")
         result.append('{:07b}'.format(ord(item)))
      elif isinstance(item, (tuple,list)):
         result.append("1")
         offset,length = item
         result.append('{num:0{width}b}'.format
                       (num=offset, width=offset_width))
         result.append('{num:0{width}b}'.
                       format(num=length, width=length_width))
   return "".join(result)

welcome_bits = intermediate2bits(welcome_intermediate)
print(welcome_bits)

def bitstring_to_file(bitstring, filename):
    bytestring = ( bitstring[i:i + 8] for i in range(0, len(bitstring), 8) )
    intstring = (int(x, 2) for x in bytestring)
    chrstring = (chr(x) for x in intstring)
    output = ''.join(chrstring)
    with open(filename,'wb') as f:
        f.write(bytes(output, 'utf-8'))

bitstring_to_file(welcome_bits, 'welcome.lz')
# !cat welcome.lz

def bits2intermediate(bitstring, window_length=2**12-1, max_rep_length=2**5-1):
    """ converts a compressed string of bits
    to intermediate compressed format """
    offset_width = math.ceil(math.log(window_length, 2))
    length_width = math.ceil(math.log(max_rep_length, 2))

    result=[]
    i = 0
    while i < len(bitstring):
        if bitstring[i] == "0":  # single ascii char
            i += 1
            ch = chr(int(bitstring[i:i + 7], 2))
            result.append(ch)
            i += 7
        elif bitstring[i] == "1":  # repeat of length >= 2
            i += 1
            offset = int(bitstring[i:i + offset_width], 2)
            i += offset_width
            length = int(bitstring[i:i + length_width], 2)
            i += length_width
            result.append((offset,length))
    return result

bits2intermediate(welcome_bits)

def lz77_decompress(compressed, window_length=2**12-1, max_rep_length=2**5-1):
    """LZ77 decompression from intermediate format to ASCII text"""
    result = ''
    i = 0
    while i < len(compressed):
        if isinstance(compressed[i], str):  # char, as opposed to a pair
            result += compressed[i]
            i += 1
        else:
            offset,rep_length = compressed[i]
            i += 1
            for j in range(rep_length):
                result += result[-offset] # fixed offset"to the left" as result itself grows
    return result

print(lz77_decompress(welcome_intermediate))

compress = lambda text: intermediate2bits(lz77_compress(text))
lz_ratio = lambda text: len(compress(text)) / (len(text)*7)

lz_ratio(welcome)

from urllib.request import urlopen

with urlopen("http://www.gutenberg.org/cache/epub/28233/pg28233.txt") as f:
    newton = f.read().decode('utf-8')
# print(newton[:newton.index('\n\r')])

newton = ''.join(ch for ch in newton if ord(ch) < 128)

# len(newton), lz_ratio(newton[:len(newton)//100])

top = perf_counter()
compress(welcome)
print(perf_counter()-top)
top = perf_counter()
compress(newton[:len(newton)//1000])
print(perf_counter()-top)
top = perf_counter()
compress(newton[:len(newton)//100])
print(perf_counter()-top)

lz77_compress("a"*40)
len(compress("a"*40))
lz77_compress("a"*40, max_rep_length=2**6-1)
lz77_compress("a"*100)
len(compress("a"*100))

k = 1000
print(len(compress('a'*k)))
print(18*((k-1)//31+1)+8)

os.system("pause")
