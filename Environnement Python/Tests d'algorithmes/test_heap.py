# -*- coding: utf-8 -*-

import os, sys

print (sys.path)

sys.path.append('C:\Python35\Algorithmique\Structure de données\Tas (Heap)')

# test module and project code

import heap
import heap_smallest

x = range(20)
heapsort(x)
assert(range(20) == x)

x = [2]
heapsort(x)
assert([2] == x)

# evaluate projects also

assert(2 == kthSmallest(range(10),3))
assert(0 == kthSmallest(range(10),1))
assert(9 == kthSmallest(range(10),10))

os.system("pause")
