# -*- coding: utf-8 -*-

import os


def string_matching_naive(text='', pattern=''):
    """Returns positions where pattern is found in text.
    We slide the string to match 'pattern' over the text
    O((n-m)m)
    Example: text = 'ababbababa', pattern = 'aba'
                     string_matching_naive(t, s) returns [0, 5, 7]
    @param text text to search inside
    @param pattern string to search for
    @return list containing offsets (shifts) where pattern is found inside text
    """

    n = len(text)
    m = len(pattern)
    offsets = []
    for i in range(n - m + 1):
        if pattern == text[i:i + m]:
            offsets.append(i)

    return offsets

os.system("pause")
