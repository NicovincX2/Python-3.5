# -*- coding: utf-8 -*-

import os


def onemode(values):
    return max(set(values), key=values.count)

os.system("pause")
