# -*- coding: utf-8 -*-

import os
import timeit

class QueueList:
    def __init__(self):
        self.lst = []
    
    def __repr__(self):
        return self.lst.__repr__()

    def push(self, value):
        self.lst.append(Node(value))

    def pop(self):
        return self.lst.pop(0)

q1 = QueueList()
q1.push(1)
q1.push(2)
q1.push(3)
print(q1.pop())
q1

class QueueLinkedList: 
  def __init__(self): 
    self.head = None 

  def __repr__(self):
        out = "["
        curr = self.head
        while curr:
            out += str(curr) + ", "
            curr = curr.next
        return out[:-2] + "]"

  def push(self, value): 
    node = Node(value)
    if self.head == None:
        self.head = node
    else:
        self.head, node.next = node, self.head
  
  def pop(self):
        if self.head != None:
            curr, prev = self.head, None
            while curr.next:
                curr, prev = curr.next, curr
            prev.next = None
            return curr.value

q2 = QueueLinkedList()
q2.push(1)
q2.push(2)
q2.push(3)
print(q2.pop())
q2

q1 = QueueList()
q2 = QueueLinkedList()
for i in range(10**5): 
    q1.push(1)
    q2.push(1)

timeit -n 100 q1.push(1)
timeit -n 100 q2.push(1)
timeit -n 100 q1.pop()
timeit -n 100 q2.pop()

class TailedQueueLinkedList: 
  def __init__(self): 
    self.head   = None 
    self.tail   = None 

  def __repr__(self):
    out = "["
    curr = self.head
    while curr:
        out += str(curr) + ", "
        curr = curr.next
    if len(out) > 2:
        out = out[:-2]
    return out + "]"

  def push(self, value): 
    node = Node(value)
    if self.head == None:
        # empty queue
        self.head, self.tail = node, node
    else:
        # push to the tail. can you think of a way to push from the head? where will you pop from?
        self.tail.next, self.tail = node, node
  
  def pop(self):
        # pop from the head
        if self.head != None:
            node = self.head
            self.head = self.head.next    
            return node.value

q3 = TailedQueueLinkedList()
q3.push(1)
q3.push(2)
q3.push(3)
print(q3.pop())
q3

q1 = QueueList()
q2 = QueueLinkedList()
q3 = TailedQueueLinkedList()
for i in range(10**5): 
    q1.push(1)
    q2.push(1)
    q3.push(1)

timeit -n 100 q1.push(1)
timeit -n 100 q2.push(1)
timeit -n 100 q3.push(1)
timeit -n 100 q1.pop()
timeit -n 100 q2.pop()
timeit -n 100 q3.pop()

os.system("pause")

