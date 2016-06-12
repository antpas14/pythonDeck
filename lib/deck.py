#!/usr/bin/python
import random
from random import randrange

SUITS_NUMBER = 4 # Number of the suits in the deck
SUITS = {} # Array containing names of the suit for type of deck 
SUITS['Italian'] = {'1' : 'Denari', '2': 'Coppe', '3': 'Spade', '4': 'Bastoni'}
SUITS['French'] = {'1' : 'Hearts', '2': 'Spades', '3': 'Clubs', '4': 'Diamonds' }

# Deck logic
class Deck:
    deck = {} # Contains an array of lenght SUITS_NUMBER 
    suits = {} # Contains a 
    suitIndex = range(1, SUITS_NUMBER + 1) # 
    def __init__(self, card_per_suits = 10, suits = 'Italian', deck_index = 0):
	self.suits = SUITS[suits]
	self.shuffle_deck()

    def shuffle_deck(self):
        self.deck = {'1':range(1,11), '2':range(1,11), '3':range(1,11), '4':range(1,11)} # For cards number
        self.suitIndex = range(1, SUITS_NUMBER + 1); # For suits 

    def check_deck_empty(self):
	return len(self.suitIndex) == 0

    def pop_card(self):
        returnObject = {}
        if not self.check_deck_empty():        
 	    # Index of the suit chosen
            innerIndex = randrange(0,len(self.suitIndex));
	    # Contains the index of the card among the card remained for the suit
            index = str(self.suitIndex[innerIndex])
            position = randrange(0, len(self.deck[index]))
            extract = self.deck[index].pop(position)
	    # If there are no other cards remaining for that suit, then remove it from deckIndex
	    if len(self.deck[index]) == 0:
                self.suitIndex.pop(innerIndex)	       
  	    returnObject['suits'] = self.suits[str(index)];
 	    returnObject['number'] = extract;
        return returnObject
