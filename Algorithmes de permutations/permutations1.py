# -*- coding: utf-8 -*-

import os

def permutations1(l):
    """Generator for list permutations.
    @param l list to generate permutations for
    @result yield each permutation
    Example:
    l = [1,2,3]
    a = [1]
    permutations1([2,3]) = [[2,3], [3,2]]
    [2,3]
    yield [1,2,3]
    yield [2,1,3]
    yield [2,3,1]
    [3,2]
    yield [1,3,2]
    yield [3,1,2]
    yield [3,2,1]
    """
    if len(l) <= 1:
        yield l
    else:
        a = [l.pop(0)]
        for p in permutations(l):
            for i in range(len(p)+1):
                yield p[:i] + a + p[i:]

if __name__ == '__main__':
    word = 'abc'
    result = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert(permutation1(word) == result)
    
    word = ''
    result = ['']
    assert(permutation1(word) == result)
    
    word = 'a'
    result = ['a']
    assert(permutation1(word) == result)

os.system("pause")