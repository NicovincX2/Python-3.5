# -*- coding: utf-8 -*-

import os

def python_bubblesort_improved(a_list):
    """ Bubblesort in Python for list objects (sorts in place)."""
    length = len(a_list)
    swapped = 1
    for i in range(length):
        if swapped: 
            swapped = 0
            for ele in range(length-i-1):
                if a_list[ele] > a_list[ele + 1]:
                    temp = a_list[ele + 1]
                    a_list[ele + 1] = a_list[ele]
                    a_list[ele] = temp
                    swapped = 1
    return a_list

os.system("pause")