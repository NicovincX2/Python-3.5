# -*- coding: utf-8 -*-

import os

from collections import Counter

given = '''ABCD CABD ACDB DACB BCDA ACBD ADCB CDAB DABC BCAD CADB CDBA
           CBAD ABDC ADBC BDCA DCBA BACD BADC BDAC CBDA DBCA DCAB'''.split()
''.join(Counter(x).most_common()[-1][0] for x in zip(*given))


from pprint import pprint as pp

pp(list(zip(*given)), width=120)
pp([Counter(x).most_common() for x in zip(*given)])
pp([Counter(x).most_common()[-1] for x in zip(*given)])
pp([Counter(x).most_common()[-1][0] for x in zip(*given)])
''.join([Counter(x).most_common()[-1][0] for x in zip(*given)])

os.system("pause")