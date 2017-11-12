#!/usr/bin/env python3

# Exercise 2: Use binary search functions (recursive and iterative).
# Genearte a random ordered list of integers and do a benchmark analysis for each one.
# What are your results? Can you explain them?

def iterative(aList, item):
    first = 0
    last = len(aList)
    found = False
    while not found and first != last:
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
                recursive(aList[midpoint+1:], item)
            else:
                recursive(aList[:midpoint], item)



