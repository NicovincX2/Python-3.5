# -*- coding: utf-8 -*-

# Imports
import os
import glob2

# Glob2 files list
all_header_files = glob2.glob('Python35/**/*.md')
print(all_header_files)

# Tri alphabétique
sep = '>> - '
for x in all_header_files:
    print(x)
    with open(x, 'r') as f:
        txt = f.read()
        if txt[-1] != '\n':
            txt += '\n'

        f.close()

        txtList = txt.split(sep)
        start = txtList.pop(0)

        triTxt = sorted(txtList)
        rep = ''
        if len(txtList) > 1:
            rep = sep + sep.join(triTxt)
        txt = start + rep
        print(txt)

        # Put in another file:
        # y = x + '.txt'
        fo = open(x, 'w')
        fo.write(txt)
        fo.close()

os.system("pause")
