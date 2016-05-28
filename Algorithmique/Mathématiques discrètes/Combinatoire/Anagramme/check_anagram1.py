# -*- coding: utf-8 -*-

import os


def sont_anagrammes(s1, s2):
    if len(s1) != len(s2):
        return False
    elif s1 == "":
        return True
    else:
        k = s2.find(s1[0])
        if k == -1:
            return False
        else:
            return sont_anagrammes(s1[1:], s2[:k] + s2[k + 1:])

print(sont_anagrammes("stainer", "tsarine"))

os.system("pause")
