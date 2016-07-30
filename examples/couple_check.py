#!/usr/bin/python

import sys
sys.path.append("../lib")
from deck import Deck

# Game logic
def couple_check():
    card_to_check = 1;
    myDeck = Deck("French", 13)
    myDeck.shuffle_deck()
    success = False
    card_1 = myDeck.pop_card()
    card_2 = myDeck.pop_card()
	
    if (card_1['number'] == card_to_check and card_2['number'] == card_to_check):
	success = True	
    return success

def main():
    successes = 0;
    failures = 0;
    while True:
        if couple_check():
            successes += 1
        else:
            failures += 1
        if ((failures + successes) % 100) == 0:
            print "FAILURES: " + str(failures) + " SUCCESSES: " + str(successes) + " PERC SUCCESSES: " + str((successes/float(successes + failures)) * 100) + " %"

if __name__ == '__main__':
    main()
