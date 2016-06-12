#!/usr/bin/python

import sys
sys.path.append("../lib")
from deck import Deck

# Game logic
def crazy_man_solitaire():
    myDeck = Deck()
    myDeck.shuffle_deck()
    fail = False
    compare_number = 1
    while not fail:
        card = myDeck.pop_card()
        if 'number' in card: # If is not in card, then deck is empty
            if card['number'] == compare_number:
                fail = True
                break
            if compare_number == 3:
                compare_number = 1;
            else:
                compare_number = compare_number + 1;
        else:
            break
    return not fail

def main():
    successes = 0;
    failures = 0;
    while True:
        if crazy_man_solitaire():
            successes += 1
        else:
            failures += 1
        if ((failures + successes) % 100) == 0:
            print "FAILURES: " + str(failures) + " SUCCESSES: " + str(successes) + " PERC SUCCESSES: " + str((successes/float(successes + failures)) * 100) + " %"

if __name__ == '__main__':
    main()
