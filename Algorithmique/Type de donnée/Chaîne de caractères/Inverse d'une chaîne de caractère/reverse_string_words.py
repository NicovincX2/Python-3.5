# -*- coding: utf-8 -*-

import os

def reverse_string_words(s):
    """Reverse words inside a string (in place).
    Since strings are immutable in Python, we copy the string chars to a list
    first.
    'word1 word2 word3' -> 'word3 word2 word1'
    Complexity: O(n)
    @param s string words to reverse.
    @returns reversed string words.
    """
    def reverse(l, i, j):
        # 'word1' -> '1drow'
        # Complexity: O(n/2)
        while i != j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1

    w = [e for e in s]
    i = 0
    j = len(w) - 1
    reverse(w, i, j)

    i = 0
    j = 0
    while j < len(w):
        while j < len(w) and w[j] != ' ':
            j += 1
        reverse(w, i, j-1)
        i = j + 1
        j += 1

    return ''.join(e for e in w)

os.system("pause")