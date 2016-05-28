# -*- coding: utf-8 -*-

import os
from bayesienne_classification import Pool

DClasses = ["clinton",  "lawyer",  "math",  "medical",  "music",  "sex"]

base = os.getcwd() + "\\learn\\"
p = Pool()
for i in DClasses:
    p.learn(base + i, i)


base = os.getcwd() + "\\test\\"
for i in DClasses:
    dir = os.listdir(base + i)
    for file in dir:
        res = p.Probability(base + i + "/" + file)
        print(i + ": " + file + ": " + str(res))

os.system("pause")
