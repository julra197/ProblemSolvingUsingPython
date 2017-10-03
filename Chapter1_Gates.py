#!/usr/bin/env python3

class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1
#Exercise 10:
class NandGate(BinaryGate):
    
    def __init__(self, n):
        BinaryGate.__init__(self,n)
    
    def performGateLogic(self): 
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 0
        else:
            return 1

class NorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 0
        else:
            return 1
        
class XorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==0 or b==1 and a==0:
            return 1
        else:
            return 0

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


#Exercise 11:
class Adder(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self, n)
        self.ouputCarry = None
        self.pinA = None
        self.pinB = None
    
    def getOutputCarry(self):
        self.outputCarry = self.performGateLogicCarry()
        return self.outputCarry

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")
    
class HalfAdder(Adder):
    def __init__(self, n):
        Adder.__init__(self, n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==0 or b==1 and a==0:
            return 1
        else:
            return 0
    
    def performGateLogicCarry(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0




def main():
   #g1 = AndGate("G1")
   #g2 = AndGate("G2")
   #g3 = OrGate("G3")
   #g4 = NotGate("G4")
   #c1 = Connector(g1,g3)
   #c2 = Connector(g2,g3)
   #c3 = Connector(g3,g4)
   #print(g4.getOutput())
   ##NAND test:
   #nand = NandGate("NAND1")
   #print(nand.getOutput())
   ##NOR test:
   #nor = NorGate("NOR1")
   #print(nor.getOutput())
   ##XOR test:
   #xor = XorGate("XOR1")
   #print(xor.getOutput())
   #HalfAdder test:
   ha1 = HalfAdder("HA1")
   print(ha1.getOutput())
   print(ha1.getOutputCarry())
   

main()
