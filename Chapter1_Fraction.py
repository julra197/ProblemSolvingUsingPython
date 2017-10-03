#!/usr/bin/env python3

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    
#Exercise 2, 5:
#Exercise 6, no changes needed, because the gcd implementation negates the numerator if the denominator is negative?
    def __init__(self,top,bottom):
        if(isinstance(top, int) and isinstance(bottom, int)):
            grCoDiv = gcd(top, bottom)
            self.num = int(top/grCoDiv)
            self.den = int(bottom/grCoDiv)
        else:
            raise ValueError("both arguments of the Fraction contructor must be integers")

    def __str__(self):
         return str(self.num)+"/"+str(self.den)

#Exercise 9:
    def __repr__(self):
        return("Fraction("+str(self.num)+", "+str(self.den)+")")
    
    def show(self):
         print(self.num,"/",self.den)

    def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum,newden)

#Exercise7: (Not working)        
    def __radd__(self, other):
        if(isinstance(other, int)):
            return Fraction(self.num+self.den*other, self.den)
        else:
            raise ValueError("Invalid types")
        
#Exercise8:
    def __iadd__(self, other):
        newNum = self.num*other.den + other.num*self.den
        newDen = self.den * other.den
        return Fraction(newNum, newDen)
    
#Exercise 3:        
    def __sub__(self, other):
        newnum = self.num*other.den - \
                      self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)
    
    def __mul__(self, other):
        return Fraction(self.num*other.num, self.den*other.den)
    
    def __truediv__(self, other):
        return Fraction(self.num*other.den, self.den*other.num)

    def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum == secondnum

#Exercise 4:        
    def __gt__(self, other):
        return (self.num/self.den)>(other.num/other.den)
    
    def __ge__(self, other):
        return (self.num/self.den)>=(other.num/other.den)
    
    def __lt__(self, other):
        return (self.num/self.den)<(other.num/other.den)
    
    def __le__(self, other):
        return (self.num/self.den)<=(other.num/other.den)
    
    def __ne__(self, other):
        return (self.num/self.den)!=(other.num/other.den)
#Exercise 1:
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den
    
firstFraction = Fraction(5, 6)
print(str(firstFraction.getDen()))
print(str(firstFraction.getNum()))

aFraction = Fraction(4, 6)
print(aFraction)

print(Fraction(3,4)-Fraction(1,2))

print(Fraction(3,4)*Fraction(1,2))

print(Fraction(3,4)/Fraction(1,2))

print("3/4 > 1/2:" + str(Fraction(3,4)>Fraction(1,2)))
print("1/2 > 1/2:" + str(Fraction(1,2)>Fraction(1,2)))
print("1/8 > 1/2:" + str(Fraction(1,8)>Fraction(1,2)))
print("1/8 > 1/2:" + str(Fraction(1,-8)>Fraction(1,2)))

print("3/4 >= 1/2:" + str(Fraction(3,4)>=Fraction(1,2)))
print("1/2 >= 1/2:" + str(Fraction(1,2)>=Fraction(1,2)))
print("1/8 >= 1/2:" + str(Fraction(1,8)>=Fraction(1,2)))

print("3/4 < 1/2:" + str(Fraction(3,4)<Fraction(1,2)))
print("1/2 < 1/2:" + str(Fraction(1,2)<Fraction(1,2)))
print("1/8 < 1/2:" + str(Fraction(1,8)<Fraction(1,2)))

print("3/4 <= 1/2:" + str(Fraction(3,4)<=Fraction(1,2)))
print("1/2 <= 1/2:" + str(Fraction(1,2)<=Fraction(1,2)))
print("1/8 <= 1/2:" + str(Fraction(1,8)<=Fraction(1,2)))

print("3/4 != 1/2:" + str(Fraction(3,4)!=Fraction(1,2)))
print("1/2 != 1/2:" + str(Fraction(1,2)!=Fraction(1,2)))
print("1/8 != 1/2:" + str(Fraction(1,8)!=Fraction(1,2)))

#secondFraction = Fraction(23.3, 7)

print(aFraction.__radd__(6))
#print(aFraction.__radd__("aString"))
#print(aFraction+6)
print("firstFraction before += : " + str(firstFraction))
print("aFraction before += : " + str(aFraction))
firstFraction += aFraction
print("firstFraction after += : " + str(firstFraction))
print(aFraction.__repr__())
aReprFraction = eval(aFraction.__repr__())
print(aReprFraction)

