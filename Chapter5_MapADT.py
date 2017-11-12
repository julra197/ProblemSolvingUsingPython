#!/usr/bin/env python3

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    # Exercise 7 Reimplement put so that the table will automatically resize itself when the loading factor
    # reaches a predefined value
    
    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))
      
        if self.loadingfactor()>0.8:
            pass
            #TODO
    
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
            while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot,len(self.slots))
    
            if self.slots[nextslot] == None:
                self.slots[nextslot]=key
                self.data[nextslot]=data
            else:
                self.data[nextslot] = data #replace
    
    def loadingfactor(self):
        return len(self)/self.size
                
    def hashfunction(self,key,size):
         return key%size
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))
      
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                             not found and not stop:
           if self.slots[position] == key:
             found = True
             data = self.data[position]
           else:
             position=self.rehash(position,len(self.slots))
             if position == startslot:
                 stop = True
        return data
      
    def __getitem__(self,key):
          return self.get(key)
      
    def __setitem__(self,key,data):
          self.put(key,data)
          
    # Exercise 4: Implement the len method (__len__):
    def __len__(self):
        counter = 0
        for slot in self.slots:
            if slot != None:
                counter += 1
        return counter
    
    # Exercise 5: Implement the in method (__contains__):
    def __contains__(self, item):
        return (item in self.data)
    
    # Exercise 6: Implement the del method:
    def __delitem__(self, key):
        searchslot = self.hashfunction(key, len(self.slots))
        stop = False
        found = False
        position = searchslot
        while not found and not stop:
            if self.slots[position] == key:
                self.slots[position] = None
                self.data[position] = None
                found = True
            else:
                position=self.rehash(position, len(self.slots))
                if position == searchslot:
                    stop = True
          
# Code to test the implementation:
H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
print(H[20])
print(H[17])
H[20]='duck'
print(H[20])
print(H.data)
print(H[99])
print("Testing the len funcion:")
print(len(H))
print("Testing the in funcion:")
print("\'tiger\' is in H:", 'tiger' in H)
print("None is in H:", None in H)
print("\'NotinH\' should evaluate to false:", 'notInH' in H)
print("Test the del function:")
print("Slots:", H.slots)
print("Data:", H.data)
del H[55]
del H[43]
print("Slots after deletion:", H.slots)
print("Data after deletion:", H.data)
print("loading Factor", H.loadingfactor())