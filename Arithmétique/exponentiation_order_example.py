# -*- coding: utf-8 -*-

import os

5**3**2

(5**3)**2

5**(3**2)

# The following is not normally done
try: from functools import reduce # Py3K
 
reduce(pow, (5, 3, 2))

os.system("pause")