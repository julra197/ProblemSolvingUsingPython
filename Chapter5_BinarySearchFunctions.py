#!/usr/bin/env python3

# Exercise 2: Use binary search functions (recursive and iterative).
# Genearte a random ordered list of integers and do a benchmark analysis for each one.
# What are your results? Can you explain them?

import random
import timeit

def iterative(aList, item):
    first = 0
    last = len(aList)-1
    found = False
    while not found and first <= last:
        midpoint = (first+last)//2
        if aList[midpoint] == item:
            found = True
        else:
            if item > midpoint:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found

def recursive(aList, item):
    if len(aList) == 0:
        return False
    else:
        midpoint = len(aList)//2
        if aList[midpoint] == item:
            return True
        else:
            if item > aList[midpoint]:
                return recursive(aList[midpoint+1:], item)
            else:
                return recursive(aList[:midpoint], item)

#Code to test the methods
testList = [1,2,3,4,5,6,7,8,9]
#print(iterative(testList, 3))
#print(iterative(testList, 23))
#print(recursive(testList, 3))
#print(recursive(testList, 23))

#Code to benchmark the functions
rlist = range(1, 100000000000)
item = rlist[random.randint(0, 99999999999)]
nir = 100000000002
print("item is in rlist using iterative:", iterative(rlist, item))
print("item is in rlist using recursive:", recursive(rlist, item))
print("nir is in rlist using iterative:", iterative(rlist, nir))
print("nir is in rlist using recursive", recursive(rlist, nir))


t1 = timeit.Timer("iterative(rlist, item)", "from __main__ import rlist, item, iterative")     
print("the iterative method lasts %.8f to find an existing item" %(t1.timeit(number=100)))
t2 = timeit.Timer("recursive(rlist, item)", "from __main__ import rlist, item, recursive")     
print("the recursive function lasts %.8f to find an existing item" %(t2.timeit(number=100)))
t3 = timeit.Timer("iterative(rlist, nir)", "from __main__ import rlist, nir, iterative")     
print("the iterative method lasts %.8f to examine the list" %(t3.timeit(number=100)))
t4 = timeit.Timer("recursive(rlist, nir)", "from __main__ import rlist, nir, recursive")     
print("the recursive function lasts %.8f to examine the list" %(t4.timeit(number=100)))

# Exercise 3. Implement the binary search using recursion without the slice operator.

def recursiveWS(aList, item):
    if len(aList) == 0:
        return False
    else:
        midpoint = len(aList)//2
        if aList[midpoint] == item:
            return True
        else:
            if item > aList[midpoint]:
                passList = []
                for i in range(midpoint+1, len(aList)):
                    passList.append(aList[i])
                return recursiveWS(passList, item)
            else:
                passList = []
                for i in range(0, midpoint):
                    passList.append(aList[i])
                return recursiveWS(passList, item)
            
#Code to test the recursiveWS method
print("\n==Ex 3: Test recursiveWS==")
print(recursiveWS(testList, 5))
print(recursiveWS(testList, 1))
print(recursiveWS(testList, 9))
print(recursiveWS(testList, 8))
print(recursiveWS(testList, 10))
