# -*- coding: utf-8 -*-

import os

print(5**3**2)

print((5**3)**2)

print(5**(3**2))

# The following is not normally done
from functools import reduce # Py3K
 
print(reduce(pow, (5, 3, 2)))

os.system("pause")