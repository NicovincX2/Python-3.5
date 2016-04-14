# -*- coding: utf-8 -*-

import os

True
not True

# As numbers
False + 0
True + 0
False + 0j
True * 3.141

# Numbers as booleans
not 0
not not 0
not 1234
bool(0.0)
bool(0j)
bool(1+2j)

# Collections as booleans
bool([])
bool([None])
'I contain something' if (None,) else 'I am empty'
bool({})
bool("")
bool("False")


os.system("pause")