# pythonDeck

This project contains a library that allow to simulate a deck of cards.
On the object Deck can be performed actions like shuffle_deck and pop_card, which returns a card data structure

Tested on Python 2.7.3 

# Applications

I implemented it because I wanted to calculate the probability of success of the "Crazy Man Solitaire".
In this game you take a deck of card (I used an Italian card deck, 40 cards, 10 cards for suit), pick the first card and say one, pick the second card and say two, piok the third card
and say "three", then when you pick the fourth card you say "one" again and so one.
If the value of the card is the same value that you said, then you have lost.
Since the user has no interaction in this game I have made an infinite loop and recorded the outcame to evaluate the probability in an empirical way.

Later I found out online the mathematical results on this Italian forum, check it out if you are curious about it:
http://www.matematicamente.it/forum/viewtopic.php?p=469119#p469119

The script used can be found in the example folder



