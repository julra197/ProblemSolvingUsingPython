#!/usr/bin/env python3

#1. Devise an experiment to verify that the list index operator is O(1)

import timeit
import random

l= list(range(10000001))   
def indexTime(pos):
        x = l[pos]

for i in range(0,10000001,1000000):
    
    t1 = timeit.Timer("indexTime(%d)"%i, "from __main__ import indexTime")
    print("list index oporation on element %d:"%i,t1.timeit(number=1000))
    
#Answer: Since the time is nearly the same, no matter which element is accessed: O(1)

print("=========================================================================================")

#2. Devise an experiment to verify that get item and set item are O(1) for dictionaries

d={k:k+2 for k in range(10000000)}
def getTest(key):
    x = d.get(key)
    
def setTest(key):
    d[key] = "Changed"
    
for i in range(0, 10000001, 1000000):
    
    t2 = timeit.Timer("getTest(%d)"%i, "from __main__ import getTest")
    print("get Operation on key %d lasts"%i, t2.timeit(number=1000))
    t3 = timeit.Timer("setTest(%d)"%i, "from __main__ import setTest")
    print("set Operation on key %d lasts"%i, t3.timeit(number=1000))
    
#Answer: Since the time is nearly the same, no matter which value is retrieved/changed, so both operations: O(1)

print("=========================================================================================")

#3. Devise an experiment that compares the permormance of the del operator on lists and dictionaries

l2= list(range(100000001))   
d2={k:k+2 for k in range(100000001)}

def delList(pos):
    del l2[pos]

def delDict(key):
    del d2[key]

for i in range(0, 10000001, 1000000):
    
    t4 = timeit.Timer("delList(%d)"%i, "from __main__ import delList")
    print("del Operation on the %d'th element of a list lasts"%i, t4.timeit(number=1))
    t5 = timeit.Timer("setTest(%d)"%i, "from __main__ import setTest")
    print("del Operation on key %d of a dict lasts"%i, t5.timeit(number=1))
    
#Answer: The del operation on a dict is faster than on a list

print("=========================================================================================")

#Given a list of numbers in random order write a linar time algorithm to find the kth smallest number in the list. Explain why your algorithm is linear


def findSmallest(ints, k):
    res=[]
    for i in ints:
        if(len(res)==0):
            res.append(i)
        else:
            put = False
            j = 0
            while not put and j<len(res):
                if i < res[j]:
                    res.insert(j, i)
                    put = True
                elif j+1==len(res):
                    res.append(i)
                    put = True
                else:
                    j = j+1
    return res[k-1]            
                   
randoms = random.sample(range(1, 1000001),1000)
print("the 3rd smallest is:", findSmallest(randoms,3))

#Answer: The algorithm is not lenear

print("=========================================================================================")

#5. Can you improve the algorithm from the previous problem to be O(n log (n))?

def findSmallestImp(ints, k):
    ints.sort()
    return ints[k-1]

randomsI = random.sample(range(1, 100000001),1000000)
print("the 3rd smallest is:", findSmallestImp(randomsI,3))

#Answer: Since the Big-O efficiency of sort is n log n and the efficiency of the index operation is O(1), the findSmallesImp allgorithms efficency is O(n log (n))



