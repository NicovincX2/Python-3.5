# -*- coding: utf-8 -*-

import os

__author__ = "bt3"

import string

def sanitize(sentence):
        array = sentence.lower()
        array = array.strip()
        array = array.strip(string.punctuation)
        return array

def check_if_palindrome(array):
        if len(array) < 2:
            return True
        
        if array[0] == array[-1]:
                return check_if_palindrome(array[1:-1])
        else:
            return False

def check_if_palindrome_iter(array):        
    i, j = 0, len(array)-1
    
    while i <= j:
        if array[i] != array[j]:
            return False
        i += 1
        j -= 1
        
    return True

def est_palindrome(s):
    if len(s)<2:
        return True
    else:
        return (s[0]==s[-1]) and est_palindrome(s[1:-1])

print(est_palindrome("biche"))

if __name__ == '__main__':
    sentence = 'hello there'
    array = sanitize(sentence)
    assert(check_if_palindrome(array) == False)
    assert(check_if_palindrome_iter(array) == False)
    
    sentence = ''
    array = sanitize(sentence)
    assert(check_if_palindrome(array) == True)
    assert(check_if_palindrome_iter(array) == True)
    
    sentence = 'h'
    array = sanitize(sentence)
    assert(check_if_palindrome(array) == True)
    assert(check_if_palindrome_iter(array) == True)
    
    sentence = 'Noel sees Leon'
    array = sanitize(sentence)
    assert(check_if_palindrome(array) == True)
    assert(check_if_palindrome_iter(array) == True)
        
    sentence = 'Noel sees Leon!'
    array = sanitize(sentence)
    assert(check_if_palindrome(array) == True)
    assert(check_if_palindrome_iter(array) == True)

os.system("pause")