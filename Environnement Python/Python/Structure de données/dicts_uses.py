# -*- coding: utf-8 -*-

import os

# create a simple dictionary
myDict = {"key1": 1, "key2": 2, "key3": 3}

print(myDict)
print(myDict["key1"])


# add a key:pair -- notice that the values can be any data type
myDict["newkey"] = "new"
print(myDict)

# and so can the keys
myDict[5] = 5
print(myDict)


# loop over the elements
for k, v in myDict.iteritems():
    print("key = %s, value = %s" % (str(k), str(v)))


# just get the keys
keys = myDict.keys()
print(keys)


# check whether a key exists
print("key1" in keys)

print("dummykey" not in keys)

os.system("pause")
