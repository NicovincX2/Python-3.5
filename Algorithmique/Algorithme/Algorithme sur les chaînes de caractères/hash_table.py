# -*- coding: utf-8 -*-


class MyHashtable:

    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.data = [[] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def find(self, item):
        """ returns True if item in hashtable, False otherwise  """
        i = self.hash_mod(item)
        try:
            self.data[i].index(item)
            return True
        except ValueError:
            return False

    def insert(self, item):
        """ insert an item into table """
        i = self.hash_mod(item)
        try:
            self.data[i].index(item)
        except ValueError:
            self.data[i].append(item)

ht = MyHashtable(100)
ht.insert("yoav")
ht.insert("amir")
ht.insert("amiram")
ht.insert("haim")
ht.find("yoav")
