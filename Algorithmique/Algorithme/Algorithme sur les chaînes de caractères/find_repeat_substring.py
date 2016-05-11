# -*- coding: utf-8 -*-

import os
from time import perf_counter
from hash_table import *

def repeat_naive(st, k):
    for i in range(len(st) - k + 1):
        for j in range(i + 1, len(st) - k + 1):
            if st[i : i + k] == st[j : j + k]:
                return True
    return False

song = '''So, so you think you can tell 
Heaven from Hell, 
Blue sky's from pain. 
Can you tell a green field 
From a cold steel rail? 
A smile from a veil? 
Do you think you can tell? 

And did they get you to trade 
Your heroes for ghosts? 
Hot ashes for trees? 
Hot air for a cool breeze? 
Cold comfort for change? 
And did you exchange 
A walk on part in the war 
For a lead role in a cage? 

How I wish, how I wish you were here. 
We're just two lost souls 
Swimming in a fish bowl, 
Year after year, 
Running over the same old ground. 
And how we found
The same old fears. 
Wish you were here.'''

print ("Repeat_naive:")
top = perf_counter()
print(repeat_naive(song, 5))
print(perf_counter()-top)
top = perf_counter()
print(repeat_naive(song, 30))
print(perf_counter()-top)

import urllib.request

with urllib.request.urlopen("http://www.gutenberg.org/cache/epub/74/pg74.txt") as r:
    book = r.read().decode('utf-8')
print(book[:book.index('\n\r')])

print ("Repeat_naive:")
top = perf_counter()
print(repeat_naive(book, 5))
print(perf_counter()-top)
top = perf_counter()
print(repeat_naive(book, 30))
print(perf_counter()-top)

def repeat_hash1(st, k, m=0):
    if m == 0: # default hash table size is ~number of substrings to be inserted
        m = len(st) - k
    htable = MyHashtable(m)
    for i in range(len(st) - k + 1):
        if htable.find(st[i : i + k]):
            return True
        else: 
            htable.insert(st[i : i + k])
    return False

print ("Repeat_hash1:")
top = perf_counter()
print(repeat_hash1(song, 5))
print(perf_counter()-top)
top = perf_counter()
print(repeat_hash1(song, 30))
print(perf_counter()-top)
top = perf_counter()
print(repeat_hash1(book, 5))
print(perf_counter()-top)
top = perf_counter()
print(repeat_hash1(book, 30))
print(perf_counter()-top)
top = perf_counter()
print(repeat_hash1(book, 1000))
print(perf_counter()-top)

def repeat_hash2(st, k, m=0):
    htable = set() # Python sets use hash functions for fast lookup
    for i in range(len(st) - k + 1):
        if st[i : i + k] not in htable:
            htable.add(st[i : i + k])
        else: 
            return True
    return False

print ("Repeat_hash2:")
top = perf_counter()
print(repeat_hash2(song, 5))
print(perf_counter()-top)
top = perf_counter()
print(repeat_hash2(song, 30))
print(perf_counter()-top)
top = perf_counter()
print(repeat_hash2(book, 5))
print(perf_counter()-top)
top = perf_counter()
print(repeat_hash2(book, 30))
print(perf_counter()-top)
top = perf_counter()
print(repeat_hash2(book, 1000))
print(perf_counter()-top)

import urllib

with urllib.request.urlopen("http://berry.engin.umich.edu/gene2oligo/lacZ.txt") as r:
    lacZ = r.read().decode('utf-8')
print(lacZ)

lacZ = str.join('',lacZ.split('\n')[2:]).upper()
print(len(lacZ))

print ("Repeat_hash1:")
top = perf_counter()
print(repeat_hash1(lacZ, 12))
print(perf_counter()-top)
print ("Repeat_hash2:")
top = perf_counter()
print(repeat_hash2(lacZ, 12))
print(perf_counter()-top)

os.system("pause")

