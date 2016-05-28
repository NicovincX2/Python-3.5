# -*- coding: utf-8 -*-

"""
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import os


def find_coll_seq(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count


def find_longest_chain(limit):
    longest, number = 0, 0
    start = 0
    while start <= limit:
        size_chain = find_coll_seq(start)
        if size_chain > longest:
            longest = size_chain
            number = start
        start += 1

    return (longest, number)


def main():
    import time
    start = time.time()

    # print(find_longest_chain(13))
    print(find_longest_chain(10**6))

    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))

if __name__ == '__main__':
    main()

os.system("pause")
