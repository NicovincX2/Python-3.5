# -*- coding: utf-8 -*-

import os

__author__ = "bt3"

def longest_increasing_subsequence1(seq):
    result, aux = [], []
    seq.append(-float('infinity'))
    
    for i, value in enumerate(seq[:-1]):
        aux.append(value)
        if value > seq[i+1]:
            if len(result) < len(aux):
                result = aux[:]
            aux = []
    return result
             
if __name__ == '__main__':
    assert longest_increasing_subsequence1([3, 4, -1, 0, 6, 2, 3]) == (4, [-1, 0, 2, 3])
    assert longest_increasing_subsequence1([10, 22, 9, 33, 21, 50, 41, 60, 80]) == (6, [10, 22, 33, 50, 60, 80])
    assert longest_increasing_subsequence1([5,0,1,2,3,4,5,6,7,8,9,10,11,12, 2, 8, 10, 3, 6, 9, 7]) == (13, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    
    seq = [10, -12, 2, 3, -3, 5, -1, 2, -10]
    result = [-12, 2, 3]
    assert(longest_increasing_subsequence1(seq) == result)
    
    seq = [2]
    result = [2]
    assert(longest_increasing_subsequence1(seq) == result)

    seq = []
    result = []
    assert(longest_increasing_subsequence1(seq) == result)

os.system("pause")