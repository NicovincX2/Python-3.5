# -*- coding: utf-8 -*-

import os
import decision_trees as dt
import networkx as nx
import numpy as np

inputs = np.zeros((16, 2))
outputs = []
row = 0
for x in range(4):
    for y in range(4):
        inputs[row][0] = x
        inputs[row][1] = y
        row += 1

for row in inputs:
    if (row[0] > 1 and row[1] < 2) or (row[0] < 2 and row[1] > 1):
        outputs.append(1)
    else:
        outputs.append(0)

clazz = [0, 1]
meta = ['x', 'y']
tree = dt.build_tree(inputs, outputs, clazz, meta)
dt.draw_tree(tree)
data = np.zeros((16, 4))
for r in range(16):
    data[r][0] = r
    data[r][1] = inputs[r][0]
    data[r][2] = inputs[r][1]
    data[r][3] = outputs[r]
# print data

import decision_trees as dt
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

p = 'D:\\Nicolas\\Python35\\Programmes\\Statistiques\\Science des données\\Exploration de données\\SAheart.data.txt'
f = open(p, 'r')
all_lines = f.readlines()
train_cnt = int(0.75 * len(all_lines))
lines = all_lines[0:train_cnt]
col_cnt = len(lines[0].split(','))
row_cnt = len(lines)
outputs = [int(line.split(',')[col_cnt - 1][0]) for line in lines]
inputs = np.zeros((row_cnt, col_cnt - 1))
for row in range(row_cnt):
    line = lines[row].split(',')[0:col_cnt - 1]
    inputs[row] = [float(v) for v in line]
clazz = [0, 1]

tree = dt.build_tree(inputs, outputs, clazz, meta=[
                     'sbp', 'tob', 'ldl', 'adip', 'famhist', 'typea', 'obes', 'alc', 'age'], max_rm=5)
# dt.draw_tree(tree)

# compare the tree precition to training values, since we haven't pruned
# this should be very accurate
diff = []
for row in range(train_cnt):
    p = dt.decide(tree, inputs[row])
    if p == outputs[row]:
        diff.append(0)
    else:
        diff.append(1)

misses = sum(diff)
print("In the training data, there were {0} miss classifications for {1} inputs, a rate of {2}%".format(
    misses, train_cnt, 100 * misses / float(train_cnt)))
x = range(train_cnt)
f, axarr = plt.subplots(2, 1)
f.subplots_adjust(right=1.5)
f.subplots_adjust(top=1.5)

# plot training comparison
ax1 = axarr[0]
ax1.scatter(x, diff)

# compare the tree prediction to actual values not used in training set
test_lines = all_lines[train_cnt + 1:len(all_lines) - 1]
actual_out = [int(line.split(',')[col_cnt - 1][0]) for line in test_lines]
row_cnt = len(test_lines)
test_in = np.zeros((row_cnt, col_cnt - 1))
for row in range(row_cnt):
    line = test_lines[row].split(',')[0:col_cnt - 1]
    test_in[row] = [float(v) for v in line]

diff = []
for row in range(len(test_in)):
    p = dt.decide(tree, test_in[row])
    if p == actual_out[row]:
        diff.append(0)
    else:
        diff.append(1)
misses = sum(diff)
print("In the hold out data, there were {0} miss classifications for {1} inputs, a rate of {2}%".format(
    misses, len(test_in), 100 * misses / float(len(test_in))))

x = range(len(diff))
ax2 = axarr[1]
ax2.scatter(x, diff)

os.system("pause")
