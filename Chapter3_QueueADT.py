#!/usr/bin/env python3

# Ex 5 Implement the Queue ADT, that the rear of the queue is at the end of the list.

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

    
q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())