# -*- coding: utf-8 -*-

import os

from itertools import combinations_with_replacement
n, k = 'iced jam plain'.split(), 2
list(combinations_with_replacement(n,k))

# Extra credit
len(list(combinations_with_replacement(range(10), 3)))

os.system("pause")