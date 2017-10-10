#!/usr/bin/env python3
import random

debug = False

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        
    def __str__(self):
        return str("%s: %s"%(self.suit, self.number))
    
    def __eq__(self, aCard):
        return self.toInteger(self.number) == self.toInteger(aCard.number)
    
    def __gt__(self, aCard):
        return self.toInteger(self.number) > self.toInteger(aCard.number)
    
    def __ge__(self, aCard):
        return self.toInteger(self.number) >= self.toInteger(aCard.number)
    
    def __lt__(self, aCard):
        return self.toInteger(self.number) < self.toInteger(aCard.number)
    
    def __le__(self, aCard):
        self.toInteger(self.number) <= self.toInteger(aCard.number)
    
    def __ne__(self, aCard):
        self.toInteger(self.number) != self.toInteger(aCard.number)
        
    def getNumber(self):
        return self.number
    
    def getSuit(self):
        return self.suit
    
    def toInteger(self, aCardNumber):
        integer = 0
        if aCardNumber == "Ace":
            integer = 14
        elif aCardNumber == "King":
            integer = 13
        elif aCardNumber == "Queen":
            integer = 12
        elif aCardNumber == "Jack":
            integer = 11
        else:
            integer = int(aCardNumber)
        return integer
    

class Deck:
    def __init__(self):
        self.allCards = []
        suits = ["Heart", "Diamond", "Club", "Spade"]
        numbers = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        for s in suits:
            for n in numbers:
                self.allCards.append(Card(s, n))
         
    def __str__(self):
        string = ""
        for card in self.allCards:
            string = string + str(card) + " "
        return string
    
    def getSize(self):
        return len(self.allCards)
    
    def getCard(self):
        return self.allCards.pop(random.randint(0, self.getSize()-1))

class Hand:
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        string = ""
        for card in self.cards:
            string = string + str(card) + " "
        return string
    
    def addCard(self, aCard):
        self.cards.append(aCard)
    
    def getCard(self):
        return self.cards.pop()
    
    def getSize(self):
        return len(self.cards)
    
class Game:
    def __init__(self):
        self.deck = Deck()
        self.hand1 = Hand()
        self.hand2 = Hand()
        self.pendingStack = Hand()
        self.player = ""
        if debug:
            print("DEBUG==============> INITIALISE GAME <===================")
            print("DEBUG====> Hand1: ",self.hand1)
            print("DEBUG====> Hand2: ",self.hand2)
            print("DEBUG====> Decksize: ", self.deck.getSize())
    
    def deal(self):
        while(self.deck.getSize() > 0):
            self.hand1.addCard(self.deck.getCard())
            self.hand2.addCard(self.deck.getCard())
        if(debug):
            print("DEBUG==============> DEAL <===================")
            print("DEBUG====> Hand1: ",self.hand1)
            print("DEBUG====> Hand2: ",self.hand2)
            print("DEBUG====> Decksize: ", self.deck.getSize())
    
    def compare(self):
        card1 = self.hand1.getCard()
        card2 = self.hand2.getCard()
        print("%s: %s vs. computer: %s"%(self.player, card1, card2))
        if debug:
            print("DEBUG==============> COMPARE <===================")
            print("DEBUG====> Card Hand1: ", card1)
            print("DEBUG====> Card Hand2: ", card2)
        if card1 > card2:
            self.hand1.addCard(card1)
            self.hand1.addCard(card2)
            print(self.player + " wins the round")
            if debug:
                print("DEBUG====> Cards added to Hand1")
            while self.pendingStack.getSize()>0:
                self.hand1.addCard(self.pendingStack.getCard())
                if debug:
                    print("DEBUG====> Card retrieved from pending stack -> added to Hand1")
        elif card1 < card2:
            self.hand2.addCard(card1)
            self.hand2.addCard(card2)
            print("The computer wins the round")
            if debug:
                print("DEBUG====> Cards added to Hand2")
            while self.pendingStack.getSize()>0:
                self.hand1.addCard(self.pendingStack.getCard())
                if debug:
                    print("DEBUG====> Card retrieved from pending stack -> added to Hand2")
        else:
            if debug:
                print("DEBUG====> Cards added pending stack")
            self.pendingStack.addCard(card1)
            self.pendingStack.addCard(card2)
            print("drawn")
    def start(self):
        print("""====================>WELCOME TO THE COMPARE CARDS GAME
              There are two payers, you and the computer.
              Both players get an equal ammount of cards.
              The higher the number of a card, the stronger is the card. The suit does not matter.
              During each round, two cards (one of each player) are compared. The player with the stronger card wins the round and get both cards.
              If both cards are of equal weight, both cards get added to a pending stack. The next winner takes also the cards of the pending stack.
              The winner is the player who get all cards. """
              )
        self.player = input("Type in your name to start the game: ")
        
    def play(self):
        self.start()
        rounds = 0
        auto = False
        while self.hand1.getSize() > 0 and self.hand2.getSize() > 0:
            if rounds != 0 and not auto:
                cont = input("Hit enter to play next round or type sth in to get the current score (hint: type in auto to simulate the game): ")
            else:
                cont = ""
            if cont == "auto":
                auto = True
            if cont == "":
                self.compare()
            else:
                print("After %d rounds: %s: %d cards, computer: %d cards. Size of the pending stack: %d"%(rounds, self.player, self.hand1.getSize(), self.hand2.getSize(), self.pendingStack.getSize()))
            rounds = rounds + 1
        if self.hand1.getSize() > 0:
            print("%s is the WINNER, congratulation!! You have played %d rounds"%(self.player, rounds))
        else:
            print("%s is the LOOSER, sorry.... You have played %d rounds"%(self.player, rounds))
def run():
    aGame = Game()
    aGame.deal()
    aGame.play()
    
run()
