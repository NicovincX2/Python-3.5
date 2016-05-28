# -*- coding: utf-8 -*-

import os

# Lists are mutable (editable) and can be sorted in place
collection = [0, '1']
# accessing an item (which happens to be a numeric 0 (zero)
x = collection[0]
collection.append(2)                  # adding something to the end of the list
collection.insert(0, '-1')            # inserting a value into the beginning
y = collection[0]                     # now returns a string of "-1"
# same as [collection.append(i) for i in [2,'3']] ... but faster
collection.extend([2, '3'])
collection += [2, '3']                 # same as previous line
# a "slice" (collection of the list elements from the third up to but not
# including the sixth)
collection[2:6]
# get the length of (number of elements in) the collection
len(collection)
collection = (0, 1)                   # Tuples are immutable (not editable)
# ... slices work on these too; and this is equivalent to collection[0:len(collection)]
collection[:]
# negative slices count from the end of the string
collection[-4:-1]
# slices can also specify a stride --- this returns all even elements of
# the collection
collection[::2]
# strings are treated as sequences of characters
collection = "some string"
# slice with negative step returns reversed sequence (string in this case).
x = collection[::-1]
# True, literal objects don't need to be bound to name/variable to access
# slices or object methods
collection[::2] == "some string"[::2]
# same as previous expressions.
collection.__getitem__(slice(0, len(collection), 2))
collection = {0: "zero", 1: "one"}    # Dictionaries (Hash)
# Dictionary members accessed using same syntax as list/array indexes.
collection['zero'] = 2
collection = set([0, '1'])            # sets (Hash)

os.system("pause")
