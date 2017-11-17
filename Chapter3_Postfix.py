#!/usr/bin/env python3

# Exercise 1 infix-to-postfix algorithm that can handle erros

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(" or symbol == ")":
            if symbol == "(":
                s.push(symbol)
            else:
                if s.isEmpty():
                    balanced = False
                else:
                    s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def mathExp(symbolList):
    valid = True
    while "(" in symbolList: 
        symbolList.remove("(")
    while ")" in symbolList:
        symbolList.remove(")")
    index = 1
    while index < len(symbolList) and valid:
        symbol = symbolList[index]
        prevSymbol = symbolList[index-1]
        if symbol in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or symbol in "0123456789":
            if not prevSymbol in ["*","/","+","-"]:
                valid = False
                #print("first DEBUG %d sym: %s prev: %s "%(index, symbol, prevSymbol))
        if prevSymbol in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or prevSymbol in "0123456789":
            if not symbol in ["*","/","+","-"]:
                valid = False
                #print("second DEBUG %d sym: %s prev: %s "%(index, symbol, prevSymbol))
        index += 1
    return valid

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    #Check the balance of parantheses
    if not parChecker(infixexpr):
        print("DEBUG: unbalanced parantheses")
        return infixexpr
    if not mathExp(tokenList.copy()):
        print("DEBUG: not a proper math expression")
        return infixexpr
 
    for token in tokenList:
        if len(token) > 1:
            #token not seperated by whitespace
            print("DEBUG: No whithespace")
            return infixexpr
        # check operators between operands
        
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("(A+B)*C-(D - E ) * ( F + G )"))
print(infixToPostfix("( A + B ) * C - D - E ) * ( F + G )"))
print(infixToPostfix("A B + C * D"))