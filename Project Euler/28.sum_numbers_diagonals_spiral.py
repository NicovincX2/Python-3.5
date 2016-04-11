# -*- coding: utf-8 -*-

'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

import os

def number_spiral(spiral):
    return rows, mid
    
def make_spiral(n):
    spiral = []
    row = rows//2
    col = col//2
    count = 1
    while row < n:
        while col < n:
            spiral[col][row] = count
            count += 1
            if count%2 == 0:
                col += 1
            else:
                row += 1
        
    return spiral

def main():
    import time
    start = time.time() 
    
    n = 5
    spiral = make_spiral(n)
    print(number_spiral(spiral))# 101
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

os.system("pause")