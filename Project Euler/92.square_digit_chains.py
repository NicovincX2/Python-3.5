# -*- coding: utf-8 -*-

'''
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
For example,
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?
'''

import os

def calculate_chain(n):
    n_str = str(n)
    while n_str != 1 or n_str != 89:
        n_str = str(n_str)
        sum_here = 0
        for d in n_str:
            sum_here += int(d)**2
        n_str = sum_here
        if n_str == 89:
            return 1
        if n_str == 1:
            return 0
        
def square_dig_chains(n):
    count = 0
    for i in range(1, n+1):
        count += calculate_chain(i)
    return count

def main():
    import time
    start = time.time() 

    print(square_dig_chains(10**7))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

os.system("pause")