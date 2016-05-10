# -*- coding: utf-8 -*-

import os

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        
    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.first = None

    def __repr__(self):
       out = "["
       curr = self.first
       while curr:
           out += str(curr) + ", "
           curr = curr.next
       return out[:-2] + "]"
        
    def length(self):
        curr = self.first
        i = 0
        while curr:
            i += 1
            curr = curr.next
        return i
            
    def prepend(self, value):
        node = Node(value)
        if not self.first:
            self.first = node
        else:
            self.first, node.next = node, self.first
    
    def append(self, value):
        node = Node(value)
        curr = self.first
        if not curr:
            self.first = node
        else:
            while curr.next:
                curr = curr.next
            curr.next = node

    def insert(self, index, value):
        curr = self.first
        for i in range(index - 1):
            if not curr or not curr.next:
                raise IndexError()
            curr = curr.next
        node = Node(value)
        curr.next, node.next = node, curr.next

    def remove(self, index):
        curr = self.first
        # iterate to the one before the one to be removed
        for i in range(index - 1):
            if not curr or not curr.next:
                raise IndexError
            curr = curr.next
        curr.next = curr.next.next
            
    def get(self, index):
        curr = self.first
        for i in range(index):
            if not curr or not curr.next:
                raise IndexError
            curr = curr.next
        return curr.value
            
    def index(self, value):
        curr = self.first
        i = 0
        while curr:
            if curr.value == value:
                return i
            curr = curr.next
            i += 1
        raise ValueError()

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
lst = LinkedList()
lst.first = node1

print(lst)
print(lst.length())
lst.prepend(0)
print(lst)
lst.append(4)
print(lst)
lst.insert(2, 1.5)
print(lst)
lst.remove(2)
print(lst)
print(lst.get(2))
print(lst.index(2))

def reverse(lst):
    prev = None
    curr = lst.first
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    lst.first = prev

print(lst)
reverse(lst)
print(lst)

os.system("pause")

