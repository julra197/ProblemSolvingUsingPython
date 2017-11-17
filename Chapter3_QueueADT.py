#!/usr/bin/env python3

# Ex 5 Implement the Queue ADT, that the rear of the queue is at the end of the list.

import timeit

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# Test code   
#q = Queue()
#q.enqueue('hello')
#q.enqueue('dog')
#q.enqueue(3)
#print(q.dequeue())
#print(q.dequeue())
#print(q.dequeue())

# Ex 6 Implement an experiment to benchmark both Queue implementations

# A queue where ther front of the queue is at the ent of the list
class QueueF:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Test code    
#q2 = QueueF()
#q2.enqueue('hello')
#q2.enqueue('dog')
#q2.enqueue(3)
#print(q2.dequeue())
#print(q2.dequeue())
#print(q2.dequeue())

#functions for the expriment:
def populate(data, queue):
    for item in data:
        queue.enqueue(item)

def retrieve(queue):
    size = queue.size()
    for i in range(0, size):
        queue.dequeue()
    

# The experiment implementation

listA = range(0, 1000000)
# Create the queues
q1 = Queue()
q2 = QueueF()
#Time the enqueue function of both queues
t1 = timeit.Timer("populate(range(0, 1000), q1)", "from __main__ import q1, populate")
print("queue1 population lasts: ", t1.timeit(number=100))
t2 = timeit.Timer("populate(range(0, 1000), q2)", "from __main__ import q2, populate")
print("queue2 population lasts: ", t2.timeit(number=100))
#Time the dequeue function of both queues
t3 = timeit.Timer("retrieve(q1)", "from __main__ import q1, retrieve")
print("queue1 retrieving lasts: ", t3.timeit(number=100))
t4 = timeit.Timer("retrieve(q2)", "from __main__ import q2, retrieve")
print("queue2 retrieving lasts: ", t4.timeit(number=100))