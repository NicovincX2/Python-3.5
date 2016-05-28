# -*- coding: utf-8 -*-

# http://nbviewer.jupyter.org/github/yoavram/CS1001.py/blob/master/recitation10.ipynb

import os
from time import perf_counter


def arithmetize(text, basis=2**16, r=2**32 - 3):
    """ convert substring to number using basis powers
    employs Horner method modulo r """
    partial_sum = 0
    for ch in text:
        partial_sum = (partial_sum * basis + ord(ch)) % r
    return partial_sum

ord("b"), ord("e"), ord("n")
arithmetize("b"), arithmetize("be"), arithmetize("ben")


def arithmetize_text_naive(text, m, basis=2**16, r=2**32 - 3):
    """ computes arithmization of all m long substrings
    of text, using basis powers """
    return [arithmetize(text[i:i + m], basis, r) for i in range(len(text) - m + 1)]


def arithmetize_text(text, m, basis=2**16, r=2**32 - 3):
    """ efficiently computes arithmetization of all m long
    substrings of text, using basis powers """
    b_power = basis ** (m - 1)
    lst = [None] * (len(text) - m + 1)
    # lst[0] equals first word arithmetization
    lst[0] = arithmetize(text[0:m], basis, r)
    for i in range(1, len(lst)):
        rolling_hash = (lst[i - 1] - ord(text[i - 1]) *
                        b_power) * basis + ord(text[i + m - 1])
        rolling_hash %= r
        lst[i] = rolling_hash  # append new_number to existing lst
    return lst

song = '''אני כל כך עצוב לי ושמש על העיר
ודיזנגוף נראה לי כמו רכבת לילה לקהיר 
בין כל הצלילים מחפש סימן 
יושב בצד הדרך 
יושב ליד הזמן 

בחדר הסגור בדידות מקיר לקיר 
ואם אצא החוצה המצב רק יחמיר 
אז אני שומע צליל מאוד מוכר 
מגיע מלמטה רחוק מהכיכר'''

print("Arithmetize_text")
print(arithmetize_text(song, 1) == arithmetize_text_naive(song, 1))
print(arithmetize_text(song, 2)[:10])
print(arithmetize_text(song, 2, 2**16 - 1)[:10])

print("Arithmetize_text_naive vs arithmetize_text")
top = perf_counter()
print(arithmetize_text_naive(song, 5))
print(perf_counter() - top)
top = perf_counter()
print(arithmetize_text(song, 5))
print(perf_counter() - top)

import urllib.request
with urllib.request.urlopen("http://www.gutenberg.org/cache/epub/2701/pg2701.txt") as f:
    book = f.read().decode('utf8')
# print(book[:book.index('\n\r\n\r')])

len(book)

print("Arithmetize_text_naive")
top = perf_counter()
arithmetize_text_naive(book[:len(book) // 10], 3)
print(perf_counter() - top)
top = perf_counter()
arithmetize_text_naive(book, 3)
print(perf_counter() - top)

print("Arithmetize_text")
top = perf_counter()
arithmetize_text(book[:len(book) // 10], 3)
print(perf_counter() - top)
top = perf_counter()
arithmetize_text(book, 3)
print(perf_counter() - top)

print("Arithmetize_text_naive")
top = perf_counter()
arithmetize_text_naive(book[:len(book) // 10], 3)
print(perf_counter() - top)
top = perf_counter()
arithmetize_text_naive(book[:len(book) // 10], 5)
print(perf_counter() - top)
top = perf_counter()
arithmetize_text_naive(book[:len(book) // 10], 10)
print(perf_counter() - top)

print("Arithmetize_text")
top = perf_counter()
arithmetize_text(book[:len(book) // 10], 3)
print(perf_counter() - top)
top = perf_counter()
arithmetize_text(book[:len(book) // 10], 5)
print(perf_counter() - top)
top = perf_counter()
arithmetize_text(book[:len(book) // 10], 10)
print(perf_counter() - top)


def find_matches(pattern, text, basis=2**16, r=2**32 - 3):
    """ find all occurances of pattern in text
    using efficient arithmetization of text """
    assert len(pattern) <= len(text)
    pattern_hash = arithmetize(pattern, basis, r)
    text_hashes = arithmetize_text(text, len(pattern), basis, r)
    return [i for i, hs in enumerate(text_hashes) if hs == pattern_hash]

matches = find_matches("moby", book.lower())
print(matches[0], len(matches), book[matches[0]:matches[0] + 4])
matches = find_matches("aye, aye, sir", book.lower())
print(matches[0], len(matches), book[matches[0]:matches[0] + 13])


def find_matches_safe(pattern, text, basis=2**16, r=2**32 - 3):
    """ find all occurances of pattern in text
    using efficient arithmetization of text """
    assert len(pattern) <= len(text)
    pattern_hash = arithmetize(pattern, basis, r)
    text_hashes = arithmetize_text(text, len(pattern), basis, r)
    matches = [i for i, hs in enumerate(text_hashes) if hs == pattern_hash and text[
        i:i + len(pattern)] == pattern]
    return matches


def foo(v, t):
    print(t)
    return v
print(foo(True, "foo") and foo(True, "bar"))
print(foo(False, "foo") and foo(True, "bar"))

text = "a" * 10**5
for pattern in ["a" * 10**2, "a" * 10**3, "a" * 10**4]:
    for f in [find_matches, find_matches_safe]:
        top = perf_counter()
        f(pattern, text)
        print(perf_counter() - top)

for pattern in ["moby", "aye, aye, sir", "moby dick was his name"]:
    for f in [find_matches, find_matches_safe]:
        top = perf_counter()
        f(pattern, book.lower())
        print(perf_counter() - top)

find_matches("da", "abracadabra", basis=2**16, r=2**16)
find_matches_safe("da", "abracadabra", basis=2**16, r=2**16)


def arithmetize_sum(text, r=2**32 - 3):
    partial_sum = 0
    for ch in text:
        partial_sum = (partial_sum + ord(ch)) % r
    return partial_sum


def arithmetize_text_sum(text, m, r=2**32 - 3):
    lst = []
    lst.append(arithmetize_sum(text[:m], r))
    for i in range(1, len(text) - m + 1):
        rolling_hash = (lst[i - 1] - ord(text[i - 1]) + ord(text[i + m - 1]))
        rolling_hash %= r
        lst.append(rolling_hash)
    return lst

print("Arithmetize_text / arithmetize_text_sum")
top = perf_counter()
arithmetize_text(song, 3)
print(perf_counter() - top)
top = perf_counter()
arithmetize_text_sum(song, 3)
print(perf_counter() - top)
top = perf_counter()
arithmetize_text(song, 30)
print(perf_counter() - top)
top = perf_counter()
arithmetize_text_sum(song, 30)
print(perf_counter() - top)

top = perf_counter()
arithmetize_text(book, 3)
print(perf_counter() - top)
top = perf_counter()
arithmetize_text_sum(book, 3)
print(perf_counter() - top)
top = perf_counter()
arithmetize_text(book, 10)
print(perf_counter() - top)
top = perf_counter()
arithmetize_text_sum(book, 10)
print(perf_counter() - top)

arithmetize_sum("I am Lord Voldemort".lower())
arithmetize_sum("Tom Marvolo Riddle ".lower())

os.system("pause")
