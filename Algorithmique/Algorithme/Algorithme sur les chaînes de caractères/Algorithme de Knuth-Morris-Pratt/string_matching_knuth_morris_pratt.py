# -*- coding: utf-8 -*-

import os

def string_matching_knuth_morris_pratt(text='', pattern=''):
    """Returns positions where pattern is found in text.
    O(m+n)
    Example: text = 'ababbababa', pattern = 'aba'
        string_matching_knuth_morris_pratt(text, pattern) returns [0, 5, 7]
    @param text text to search inside
    @param pattern string to search for
    @return list containing offsets (shifts) where pattern is found inside text
    """
    n = len(text)
    m = len(pattern)
    offsets = []
    pi = compute_prefix_function(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q = q + 1
        if q == m:
            offsets.append(i - m + 1)
            q = pi[q-1]

    return offsets

os.system("pause")